#!python
#  purpose: create an html file to show 2 side by side columns that
#  collapses to 1 table stacked on the of the second
#  this uses the bootstrap programming framework
import os
import sys
from externFunc import printHtmlHead,printTableEnd, printTableStart
from externFunc import printDocumentEnd, includeExternalCss

with open(r"c:\tmp\addedInfo", 'r') as fp:
    addedInfo = fp.read()
    fp.close()

with open(r"c:\tmp\covidStats", 'r') as fp:
    lines = fp.readlines()
    linesRead = len(lines)
    fp.close()

# read the first line which contains the date the covidStats file was create
# and leave the file pointer pointer to second lines

# for elem in lines:
#     dateOfRawData = elem
#     break
dateOfRawData= lines[0]

printHtmlHead(dateOfRawData)
printTableStart()

skipFirstLine=True
linesPerCol = 1
linesPrinted = 1

# lineRead was the number of lines read. Ignore the first line
# because it contained the date of the covid data
linesRead -= 1

for elem in lines:
    if skipFirstLine == True:
        skipFirstLine = False
        continue
    
    first_column=True

    # each element has 2 fields
    for field in elem.split():
        
        # Hood River is always the first column
        if field == 'Hood-River':
            """ change table entry color """
            print('<tr class="table-success" style="font-weight: bold; font-style: italic;">')

        elif first_column == True:
            print('<tr>')

        # we're here outputting the 'FIRST' field of the line which is the county name
        # so print without a CR(carriage return)to save the number of lines in the output
        print("<td>{}</td>".format(field),end='')
        linesPerCol += 1
        first_column = False

    print("</tr>")

    # linesPerCol is incremented twice per line printed
    # so jumping to the next column is same as printing
    # only half the entries in first column - linesPerCol
    # needs to be resetted so as to not execute this block
    # of code again
    
    if linesPerCol > linesRead:
        printTableEnd()
        printTableStart()
        linesPerCol = 0

# end of for ele in lines loop

printTableEnd()
printDocumentEnd()

