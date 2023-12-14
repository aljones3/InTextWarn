# Personalized Content Warning Generator
Project by Aleister Jones and Athena Gundry

## Introduction

The goal of this project is to provide a customizable tool for generating content warnings in documents. Many people find content warnings useful, including people with PTSD (post-traumatic stress disorder), people who have recently experienced a traumatic event, and people with severe phobias. Unfortunately, content warnings are rarely provided in any form of media, and when they are provided they often only warn for a few topics, which does not cover the varying needs of  people who need content warnings. This forces people to choose between the possibility of running into upsetting content by surprise and avoiding new media altogether. 

The tool we developed allows users to build fully custom lists of words and phrases that they want warnings for, and to generate both in-text content warnings and summaries of how many times different categories of content are flagged in a word document. Lists can be shared between people and tweaked to each individual's needs. The tool can currently be used in the command line, and has the potential to be built into other user interfaces. 

## Related Work

### First-Person Accounts

We found multiple first person accounts attesting to the need for content warnings. For instance, [here is an article by a sexual assault survivor](https://devonprice.medium.com/hey-university-of-chicago-i-am-an-academic-1beda06d692e) and teacher about why he tells students they can ask him to warn them before content they personally find upsetting is brought up in class. He explains that he thinks content warnings are useful from his personal experience as a survivor, and that content warnings have a positive impact on his students’ ability to learn and engage with difficult class material.

Phobias are another reason people might need content warnings. For instance, [here is a reddit post by someone with emetophobia](https://www.reddit.com/r/emetophobia/comments/12a8uv3/wish_people_put_trigger_warnings_on_videos_with_v/) (fear of vomiting) saying they wish content including depictions of vomiting was warned for because encountering it by surprise is upsetting

### Similar Tools

Searching for similar tools online, we found a few [browser extensions that provide content warnings for websites](https://chromewebstore.google.com/detail/warn-me/koglokeamlegaaidhjnjdbifcpnkoafg?pli=1) and [online lists of community-sourced content warnings](https://www.doesthedogdie.com), but we didn’t find anything that would provide content warnings on digital documents. Digital documents include all sorts of important content like readings for school, documents for work, and books and textbooks, so our tool is addressing an unmet need. Since our tool uses custom words, it’s also particularly useful for people who need warnings for uncommon topics that aren’t included in community-sourced content warnings.

## Disability Justice

### Recognizing Wholeness
The disability justice principle recognizing wholeness states that disabled people are full people with complex thoughts, feelings, and lives. Our project gives disabled people who need to be warned of certain content a tool to assess the content of text files, letting them access books, papers, and other interesting texts with a decreased risk of being surprised by upsetting content. Well-known books often have community-sourced content warnings posted online, which is an awesome resource, but isn’t helpful for niche texts that haven’t gotten content warnings. Our project aims to help fill in this gap. This follows the principle of recognising wholeness because it recognizes that people who need content warnings have just as much desire and need to read as anyone else, and should be able to minimize risks to their mental health while doing so.

### Collective Access
The principle of collective access states that accessibility is a community responsibility and that we must work to support each others’ access needs. The principle specifically notes that “we can balance autonomy while being in community”. Our project supports the autonomy of people who need content warnings by giving them a tool to assess content on their own instead of relying on other people to give them accurate warnings. Community efforts for content warnings are very valuable, but cannot meet the specific needs of every single person, because different people need different warnings and want to access totally different texts. Our project compliments these community efforts, meeting some of the needs they cannot. This combination of strategies to meet different access needs is an example of collective access.

## Methodology

### Tool Overview
The content warning generator we developed is currently a command line tool. The user inputs a word document, a text document containing the search terms they want to use, and a location to write a new version of the document with in-text warnings to. Search terms can be grouped into categories, and only the category titles are displayed in warnings. The user can choose whether they want warnings before every paragraph, before the first occurrence of each category, or no warnings (in which case no copy of the inputted document is made and the user just receives a summary of the number of times each category was flagged printed to the command line). 

![A graphic of three pages of text, the first labeled document, the second labeled search terms, and the third labeled warnings added. A plus symbol and an arrow indicate the document and search terms are combined to generate the page with warnings added. The original document has three paragraphs, one of which mentions cats. The document of search terms has two lists of search terms, one of terms related to cats and one of terms related to dogs. The page with warnings added is a copy of the original document with a warning reading Warning: content in this paragraph may include cats. before the paragraph that mentions cats. There is not a warning for dogs.](https://i.ibb.co/mHyhDQ4/Screenshot-2023-12-13-at-21-09-21.png)

The image above shows the general process: the user inputs a word document and a list of search terms, and they receive a document with content warnings added where relevant.

Search term documents are text documents with a particular format: each category of search terms is separated by a line with only a '-' on it, and each search term is placed on a different line. The first term in each category is the category title, which will be displayed in warnings but not searched for, and all other terms are searched for. Terms can contain multiple words, and if they do the tool will check whether all of the words in the term occur close to each other in the document searched. These files can be saved, tweaked to people's preferences, and shared. The tool also checks for different forms of the same word. For instance, if "cat" is included in the search terms the tool will also warn for the word "cats". 
### Backend

We built our tool in Python. It uses the python-docx library to read from and write to word documents. It also uses the nltk (natural language toolkit)'s SnowballStemmer to "stem" words, removing prefixes and suffixes to get to the main meaning of the word. The algorithm turns "cats" into "cat" and "running" into "run", for instance. This allows our program to recognize words that refer to the same topic in plural or in a different tense. We designed a data structure to represent a set of categories and search terms, wrote a method that reads a properly formatted document into said data structure, and wrote a search algorithm that searches for words and phrases inputted via said data structure. We built our command line program using these methods.


### Validation

**Warning: this section contains terms related to sexual assault in the context of testing our program.**


We decided to test our program by generating warnings for a topic many people would like to be warned of, sexual assault. We tested our program on 55 paragraphs of text across 3 informative articles. 2 of the articles discussed sexual assault and the other discussed non-sexual violence. We tried three different lists of search terms, a short list with just the term 'sexual assault', a medium list with 6 obvious terms, and a long list of 10 terms built from searching for related terms on the internet.
| search word list | true positives |true negatives |false positives|false negatives|
|--|--|--|--|--|
| short list (1 term) |  9|34|0|12|
| medium list (6 terms) | 17 |34 |0|4|
| long list (10 terms) | 21 |34|0|0|

We did not get any false positives, and with a list of 10 terms our program accurately identified every mention of sexual assault in a set of informative articles.

There was one situation in which our tool did not produce useful results, though: fiction that described sexual assault without using any words that refer specifically to sexual assault. We tested such an excerpt against all three term lists, and unsurprisingly none flagged any of the text as containing mentions of sexual assault. In such cases the triggering content is comprised of detailed description using common words, not words specifically related to sexual assault or other triggers. With this in mind, our tool is effective primarily for texts that use direct language, especially when it comes to broad concepts like sexual assault. It is effective at checking for more wording-specific content like mentions of specific objects in any type of text. For situations where our tool is not very effective, crowdsourced content warnings are often a good alternative since they do not rely on specific word use. AI might also have the potential to more effectively find non-wording-based triggering content. 

Given the short timeline of this project we were not able to do any user testing beyond using the program ourselves. If this project were to continue it would be important to get feedback from people who need content warnings and would potentially find a content warning generator useful.

## Learnings and Future Work


We learned through this project that searching for particular content is a very complex task. Since words can have completely different meanings in different contexts and concepts can be described in detail without language specific to the concept, just searching for variations on words doesn't get you a full picture of the meaning of a text. This also makes matching synonyms very difficult. We hoped to match words to synonyms and similar words to reduce the number of terms users would need to include in their search term lists, but were unsuccessful. We tried using word vectors, which assign words a numerical value based on their meaning, but word type was weighed too heavily: "dog" and "cat" were deemed more similar than "dog" and "dogs". We also tried just using synonym lists, but since synonyms depend on context the lists we could find included terms completely unrelated to what we were trying to search for, like "computerized axial tomography" (the "CAT" in "CAT scan") as a synonym for "cat". 

This suggests we would need to branch out from simple text scanning to make a more accurate content warning generator. Word vectors are a form of Natural Language Processing (NLP), machine learning used to interpret language, and while word vectors weren't right for our purposes, more complex NLP might get better results. More advanced forms of NLP, which include AI like ChatGPT, might be useful in developing a search that identifies the meaning of text instead of relying on word matching. A nicer user interface would also be an obvious improvement to our current tool, and our code is set up to make a user interface easy to implement.

## Accessibility Features

Since our tool is run using the command line, the user interface is entirely text, which is an accessible format. The main complexity is figuring out what information the command needs and how to format it. We documented our code including detailed operating instructions that explain how the user needs to format their command. We also designed our command to take in a text file containing lists of terms to search for instead of taking the terms as command line arguments, allowing users to save and reuse sets of terms. This decreases the amount of typing needed to run the program, means users don't have to remember all terms they want to search for, means users have the option of using lists of terms written by other people, and makes building long lists of search words manageable. 

## Download

[You can find our code here](https://github.com/aljones3/InTextWarn/tree/main) if you would like to try it out.
