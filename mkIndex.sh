#!bash

#
# need a file named full.data - its created by copy and paste from
# oregon email notice
#

# call this function defined below
#

BUILD_DIR='.tmp'

function getRawData()
{
	rm -f $BUILD_DIRfull.data
	echo paste covid data, followed by ^D
	cat > $BUILD_DIR/full.data
}

rm -rf $BUILD_DIR
mkdir $BUILD_DIR
echo this script is depending on the user have the raw data
echo stored in the clipboard, the paste function will retrieve it
echo calling getRawData function to create full.data

getRawData		# call this function

cat $BUILD_DIR/full.data | sed -e 's|\\|/|g' > $BUILD_DIR/full-data

./mk2files.sh	# create files: rawdata and addedInfo

#
# convert rawdata file to covidStats
./raw2tuples.sh

rm -f c:/tmp/index.html

# read files: addedInfo and covidStats to create index.html
./mkCovid-webpage.py  > c:/tmp/index.html

#
# python routine to lauch a webpage
# ---------------------------------
python -c '
import webbrowser
url="c:\\tmp\\index.html"
print(url)
webbrowser.open(url, new=1)
'
# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  --app=http://192.168.1.79:/index.html