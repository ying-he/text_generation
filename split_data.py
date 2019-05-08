# -*- coding: utf-8 -*-
# Author: HeYing
# Creation Date: 2019-04-21

import pandas as pd
import os

quora = pd.read_csv('quora_duplicate_questions.tsv',sep="\t",header=0)
quora = quora.dropna()
quora.question1 = quora.question1.str.strip()
quora.question2 = quora.question2.str.strip()
quora.to_csv('clean_data.csv',sep='\t',index=False)

count=0
chunkrows = 2000  # read 2k rows at a time
headers = ["id","qid1","qid2","question1","question2","is_duplicate"]
df = pd.read_csv('clean_data.csv', sep='\t',header=0,iterator=True, chunksize=chunkrows)
os.mkdir('raw')
for chunk in df:  # for each 2k rows
    outname = 'raw/split_%d.csv'%count
    #append each output to same csv, using no header
    chunk.to_csv(outname, mode='a', header=headers, index=None,sep='\t')
    count+=1
