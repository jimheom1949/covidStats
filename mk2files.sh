#!bash
#mk2files.sh

rm -f tmp.data
tmp=$$
tr '\n' ' ' < .tmp/full-data > $tmp
sed 's/\(counties:\)/\1\n/' $tmp > tmp.data
python -c '
fp = open("tmp.data")
a=fp.readline().strip()
b=fp.readline().strip()
fp.close()
fp = open(".tmp/addedInfo","w")
fp.write(a)
fp.close()
fp = open(".tmp/rawdata","w")
fp.write(b)
fp.close()
'
rm -f $tmp tmp.data
