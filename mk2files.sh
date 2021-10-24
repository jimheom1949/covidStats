#!bash
#mk2files.sh

rm -f tmp.data
tmp=$$
tr '\n' ' ' < /c/tmp/full.data > $tmp
sed 's/\(counties:\)/\1\n/' $tmp > tmp.data
python -c '
fp = open("tmp.data")
a=fp.readline().strip()
b=fp.readline().strip()
fp.close()
fp = open("addedInfo","w")
fp.write(a)
fp.close()
fp = open("rawdata","w")
fp.write(b)
fp.close()
'
rm -f $tmp tmp.data
