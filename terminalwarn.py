from docxwarn import *
import sys

# This command-line method uses the structures defined in docxwarn.py to
# provide a  simple content warning generator that scans documents for an
# inputted list of words/phrases to be warned for. 

# usage: "terminalwarning.py input_file search_terms mode output_file".
# scans input_file for the words/categories in search_terms, prints a summary
# of occurances to the terminal, and writes a copy of input_file containing
# in-line content warnings to output_file. WILL OVERWRITE OUTPUT_FILE.

# input_file and output_file should be word documents (.docx)
# search_terms should be a properly formatted txt file
# modes: 
#   'every': places a warning before every paragraph flagged
#   'first': places a warning before the first paragraph flagged for each category
#   'none' (or any other input): no change to output file

# notice that search term files can be built, reused, and shared!
# don't need to include mode/output_file if you don't want in-line warnings

# search_terms format: words should be seperated by line breaks. multi-word
# phrases can be entered on the same line, and the tool will search for
# the set of words occuring close to each other. categories can be defined
# by seperating each category with a '-' line. the first word in a category
# is the title and will not be searched for, all other words are searched for.
def main():
    doc = Document(sys.argv[1])
    terms = listFromTxtStump(sys.argv[2])
    if len(sys.argv) < 4:
        mode = " "
    else:
        mode = sys.argv[3]
    if len(sys.argv) < 5:
        newdoc = ""
    else:
        newdoc = sys.argv[4]
    totals = searchDocxStump(doc, newdoc, terms, mode)
    print("WARNING SUMMARY:")
    for cindex, cat in enumerate(terms.getCats()):
        print(cat + ": " + str(totals[cindex]) + " flags")

if __name__ == "__main__":
    main()