# -*- coding: utf-8 -*-
# Author: HeYing
# Creation Date: 2019-04-19

import time
import datetime
from googletrans import Translator
import pandas as pd
pd.set_option('display.max_colwidth', 700)

def main(inputfile, outputfile):
    # 设置随机域名
    translator = Translator(service_urls=['translate.google.cn', 'translate.google.co.jp', 'translate.google.co.kr'])
    starttime = datetime.datetime.now()
    preDir = "~/quoraTranslation/"
    dataDir = preDir + inputfile
    quoraData = pd.read_csv(dataDir, sep='\t', header=0)
    n = len(quoraData['id'])  # 样本长度
    print("数据集共有 %d 对句子." % n)
    # 储存翻译后的中文问题
    zhQuestion1 = []
    zhQuestion2 = []
    for i in range(n):
        ques1 = quoraData.at[i, 'question1']
        # print(ques1)
        ques2 = quoraData.at[i, 'question2']
        while 1:
            # 删去句号. 问号? 感叹号!之后的空格
            ques1 = ques1.replace(". ", ".").replace("? ", "?").replace("! ", "!")
            ques2 = ques2.replace(". ", ".").replace("? ", "?").replace("! ", "!")
            if ques1 == "q!" or ques2 == "q!":
                break
            zhQues1 = translator.translate(ques1, dest="zh-cn").text
            zhQues2 = translator.translate(ques2, dest="zh-cn").text
            zhQuestion1.append(zhQues1)
            zhQuestion2.append(zhQues2)
            break
        time.sleep(1)
        print(i)
    quoraData['zhQuestion1'] = zhQuestion1
    quoraData['zhQuestion2'] = zhQuestion2
    newDir = preDir + outputfile
    quoraData.to_csv(newDir, index=False)
    endtime = datetime.datetime.now()
    print((endtime - starttime))


if __name__ == "__main__":
    main()