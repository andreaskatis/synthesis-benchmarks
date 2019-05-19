for file in *.lus
do
  echo "$file" >> results.txt
  jrealizability -timeout 9000 -fixpoint_T -scratch "$file" >> results.txt
done
