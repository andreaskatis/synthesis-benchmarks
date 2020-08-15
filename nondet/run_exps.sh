#!/bin/bash
for f in *.lus; do
    echo "Running JSYN-VG on $f";
	jrealizability -fixpoint -synthesis -timeout 1000 $f
done