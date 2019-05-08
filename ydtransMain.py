# -*- coding: utf-8 -*-
# Author: HeYing
# Creation Date: 2019-04-21

import datetime
from ydtrans import translate
import pandas as pd
import time 
pd.set_option('display.max_colwidth', 1000)

def format_ques(trans_result):
    '''
    input: trans_result: result from youdao translate(a dict-like string)
    output: structured chinese question
    '''
    trans_dict = eval(trans_result)
    result = []
    for i in trans_dict['translateResult']:
        text = ''
        for j in range(len(i)):
            #为了处理'Is Kristen Stewart a bad actress?  Why or why not?\nIs Jennifer Lawrence a bad actress?'这种情况
            text += i[j]['tgt']
        result.append(text)
    return result


def main():
    # starttime = datetime.datetime.now()
    import os
    preDir = "./raw/"
    postDir = "./chinese/"
    if not os.path.isdir(postDir):
        os.mkdir(postDir)

    for cur_ind in range(0,203):
        dataDir = preDir+"split_%d.csv"%cur_ind
        quoraData = pd.read_csv(dataDir, sep='\t', header=0)
        n = len(quoraData['id']) # 样本长度
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
                ques1 = repr(ques1).replace(". ", ".").replace("? ", "?").replace("! ", "!").replace('\\','')
                ques2 = repr(ques2).replace(". ", ".").replace("? ", "?").replace("! ", "!").replace('\\','')
                if ques1 == "q!" or ques2 == "q!":
                    break
                
                ch_ques = None
                while ch_ques is None:
                    try:
                        trans_result = translate(ques1+'\n'+ques2)
                        print(trans_result)
                        ch_ques = format_ques(trans_result)
                    except :
                        pass
                zhQues1 = ch_ques[0]
                zhQues2 = ch_ques[1]
                zhQuestion1.append(zhQues1)
                zhQuestion2.append(zhQues2)
                break
            print(i)
            time.sleep(0.1)
        quoraData['zhQuestion1'] = zhQuestion1
        quoraData['zhQuestion2'] = zhQuestion2
        postname = postDir+"split_%d.csv"%cur_ind
        quoraData.to_csv(postname, index=False,sep='\t')
        #endtime = datetime.datetime.now()
        #print((endtime - starttime))


if __name__ == "__main__":
    main()

