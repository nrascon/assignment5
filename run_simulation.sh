#!/bin/bash

for i in 1 2 4 8 16
do
    for j in 1 2 3 4 5 6
    do
        gem5 --outdir=$j-algorithm-$i-cores-output run.py --cores=$i --algorithm=$j
    done
done