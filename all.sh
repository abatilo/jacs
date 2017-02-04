for f in `ls text/*.txt`; do
  head -n -20 $f >> all.txt
done
