import re
from docx import *
from nltk.stem.snowball import SnowballStemmer

# This document contains a set of methods and a data structure designed to facilitate
# personalized content warning generation. These methods are used by terminalwarn.py,
# and could also be incorporated into a cleaner user interface.


# This class represents a set of categories of words/phrases. Each category has a
# title and a set of phrases associated with that title. 
class searchListMulti:
    def __init__(self):
        self.categories = [] # set of category titles
        self.words = [] # lists of phrases for each category, associated by index
        self.maxLength = 0 #length of longest phrase in the list

    # add a new category titled [cat] to this searchList. does nothing if [cat]
    # is already a category in this list.
    def addCat(self, cat):
        if not cat in self.categories:
            self.categories.append(cat)
            self.words.append([])

    # add a new word or phrase into the [cat] category of this searchList.
    # multi-word phrases should be inputted as a single string seperated by spaces.
    # does nothing if [cat] is not a category in this list.
    def addWord(self, cat, word):
        word = word.lower()
        # splits sentance into list of words
        words = word.split()
        words = list(filter(None, words))
        if cat in self.categories:
            idx = self.categories.index(cat)
            if words not in self.words[idx]:
                self.words[idx].append(words)
                # update max length
                if len(words) > self.maxLength:
                    self.maxLength = len(words)

    # returns a list of the categories in this searchList
    def getCats(self):
        return self.categories
    
    # returns a list of the phrases in the category [cat]
    def getWords(self, cat):
        if cat in self.categories:
            return self.words[self.categories.index(cat)]
    
    # returns the length of the longest phrase in this structure
    def getMaxLength(self):
        return self.maxLength

snow_stemmer = SnowballStemmer(language='english')

# this method reads a properly formatted text file [f] into a searchListMulti
# and returns said searchListMulti. it 'stumps' words before adding them, which
# removes modifiers like 'ing', and 's' to get the base word. "cats" stumps to
# "cat", for instance. using stumped words to search for content decreases the
# number of words users have to add to their text file.

# search_terms format: words should be seperated by line breaks. multi-word
# phrases can be entered on the same line, and the tool will search for
# the set of words occuring close to each other. categories can be defined
# by seperating each category with a '-' line. the first word in a category
# is the title and will not be searched for, all other words are searched for.
def listFromTxtStump(f):
    file = open(f, 'r')
    retList = searchListMulti()
    lines = file.readlines()
    lines = list(filter(None, lines))
    currCat = ""
    for line in lines:
        line = line.strip()
        if (line == '-'):
            currCat = ""
        else:
            if currCat == "":
                currCat = line
                retList.addCat(line)
            else:
                retList.addWord(currCat, snow_stemmer.stem(line))
    return retList

# this method searches the word document [input] for the words in searchListMulti
# [terms], returning a list of the number of flagged words in each category that
# corresponds via index to the category list in [terms]. words in [input] are
# stumped before comparison. multi-word phrases are flagged if the words all occur
# within [factor] * the phrase length of each other. [input] should be a python-docx
# Document. if mode is chosen accordingly, this method will write a copy of [input]
# that contains inline content warnings to [output].

# modes: 
#   'every': places a warning before every paragraph flagged
#   'first': places a warning before the first paragraph flagged for each category
#   'none' (or any other input): no change to output file
def searchDocxStump(input, output, terms, mode = '', factor = 2):
    if output == "":
        mode = ''
    categories = terms.getCats()
    totals = [0] * len(categories)
    # iterate over words in paragraph
    for p in input.paragraphs:
        text = re.split('\W+', p.text.lower())
        text = list(filter(None, text))
        warnList = []
        prevWords = [] #stored word history for sentance matching
        max = int(terms.getMaxLength() * factor) # max number of words we need to store

        # check current words against search sentances
        for x in text:
            xStump = snow_stemmer.stem(x)
            # update word history
            prevWords.append(xStump)
            if len(prevWords) > max:
                prevWords.pop(0)

            # check for sentances
            for cindex, cat in enumerate(categories):
                for words in terms.getWords(cat):
                    # check if current word is in this sentance
                    if xStump in words:
                        # if it is, check if whole sentance is in [factor] prev words
                        if set(words).issubset(prevWords[-(int(len(words) * factor)):]):
                            totals[cindex] = totals[cindex] + 1
                            if not cat in warnList:
                                if (mode == "every") or (mode == "first" and totals[cindex] == 1):
                                    warnList.append(cat)

        if len(warnList) > 0:
            if mode == "every":
                p.insert_paragraph_before("Warning: content in this paragraph may include " + 
                                          ", ".join([str(x) for x in warnList]) + ".")
            if mode == "first":
                p.insert_paragraph_before("Warning: content beyond this point may include " + 
                                          ", ".join([str(x) for x in warnList]) + ".")
                
    if mode == "every" or mode == "first":
        input.save(output) 
    return totals