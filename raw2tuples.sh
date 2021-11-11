#!bash
echo "This scripts checks the existence of the messages file."
echo "Checking..."

BUILD_DIR='.tmp'

function addLeadingZeros()
{
  # add leading zero to allow sort routine to sort covid case numbers correctly
  awk 'match($0, /[0-9]+/) {
    x = substr( $0, RSTART, RLENGTH )
    printf("%s %03d\n", $1, x)}'
}

if [ -f $BUILD_DIR/rawdata ]
  then
    echo "rawdata file exists."
else
    echo no rawdata
    exit
fi
rm -f $BUILD_DIR/covidStats
date +%m-%d-%Y > $BUILD_DIR/covidStats
cat $BUILD_DIR/rawdata |
sed -e 's/[()]//g' -e 's/ and/\n/' -e 's/\.$//'|
tr '.' '\n' | tr ',' '\n' |
sed -e 's/Hood River/Hood-River/'| 
addLeadingZeros |
sort -r -k2 |
sed -e 's/ 0*/ /' >> $BUILD_DIR/covidStats

echo "created $BUILD_DIR/covidStats"
