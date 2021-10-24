#!bash

#
# need a file named full.data - its created by copy and paste from
# oregon email notice
#

# call this function defined below
#
./mk2files.sh	# create files: rawdata and addedInfo

#
# convert rawdata file to covidStats
./raw2tuples.sh

rm -f c:/tmp/index.html

# read files: addedInfo and covidStats to create index.html
c:/tmp/mk2colwebpg.py > c:/tmp/index.html

#
# python routine to lauch a webpage
# ---------------------------------
python -c '
import webbrowser
url="c:\\tmp\\index.html"
print(url)
webbrowser.open(url, new=1)
'
