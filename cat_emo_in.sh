#!/bin/bash
cat     emo_in_01_A.csv >  emo_in_01_AB.csv
tail +2 emo_in_01_B.csv >> emo_in_01_AB.csv
cat     emo_in_02_A.csv >  emo_in_02_AB.csv
tail +2 emo_in_02_B.csv >> emo_in_02_AB.csv
cat     emo_in_03_A.csv >  emo_in_03_AB.csv
tail +2 emo_in_03_B.csv >> emo_in_03_AB.csv
cat     emo_in_04_A.csv >  emo_in_04_AB.csv
tail +2 emo_in_04_B.csv >> emo_in_04_AB.csv
