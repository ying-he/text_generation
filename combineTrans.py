# -*- coding: utf-8 -*-
# Author: HeYing
# Creation Date: 2019-04-25

import pandas as pd

preDir = "./chinese/split_"
posDir = ".csv"
filenames = []
for i in range(203):
    fileDir = preDir + str(i) + posDir
    filenames.append(fileDir)
print("\n".join(filenames[:20]))

allframes = []
for file in filenames:
    filedata = pd.read_csv(file, sep='\t', header=0)
    allframes.append(filedata)
resultFrame = pd.concat(allframes)
resultName = "./quoraTransDataset.csv"
resultFrame.to_csv(resultName, index=False, sep='\t')

