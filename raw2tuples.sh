#!bash
echo "This scripts checks the existence of the messages file."
echo "Checking..."
tmpDir='c:/tmp'
ls $tmpDir/rawdata
if [ -f $tmpDir/rawdata ]
  then
    echo "rawdata file exists."
else
    echo no rawdata
    exit
fi
\rm -f covidStats
date +%m-%d-%Y > $tmpDir/covidStats
cat rawdata |
sed -e 's/[()]//g' -e 's/ and/\n/' -e 's/\.$//'|
tr '.' '\n' | tr ',' '\n' |
sed -e 's/Hood River/Hood-River/'|
# add leading zero to allow sort routine to sort covid case numbers correctly
./leadingZeros.sh | sort -r -k2 | sed -e 's/ 0*/ /' >> $tmpDir/covidStats

echo "...done."
