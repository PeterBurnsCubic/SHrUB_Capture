#!/bin/bash
if [ $# -eq 0 ]; then
   echo "Usage: $0 log_file_name_stem"
   echo "where log_file_name_stem is one of emo_in, emo_out etc."
   exit
fi
cat     $1_01_A.csv >  $1_01_AB.csv
tail +2 $1_01_B.csv >> $1_01_AB.csv
cat     $1_02_A.csv >  $1_02_AB.csv
tail +2 $1_02_B.csv >> $1_02_AB.csv
cat     $1_03_A.csv >  $1_03_AB.csv
tail +2 $1_03_B.csv >> $1_03_AB.csv
cat     $1_04_A.csv >  $1_04_AB.csv
tail +2 $1_04_B.csv >> $1_04_AB.csv
