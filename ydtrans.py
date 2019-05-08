# -*- coding: utf-8 -*-
# Author: HeYing
# Creation Date: 2019-04-21

import hashlib
import time
import requests
import random
from requests.adapters import HTTPAdapter

def createData(transStr):
    '''
    待翻译的内容
    :param transStr: 
    :return: dict
    '''
    salt = str(int(time.time()*1000))+str(random.randint(0,9))
    client = 'fanyideskweb'
    a = "@6f#X3=cCuncYssPsuRUE"
    md5 = hashlib.md5()
    digStr = client+transStr+salt+a
    md5.update(digStr.encode('utf-8'))
    sign = md5.hexdigest()
    
    # data里的参数from, to可以设置输入语言以及目标翻译语言
    data = {
        'i': transStr ,
        'from': 'en',
        'to': 'zh-CHS',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts' : int(salt)//10,
        'bv' : ,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
        
    }
    return data
def translate(text_to_trans):
    #construct headers
    #这里不应缩进
    header_text = '''
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent:
X-Requested-With: XMLHttpRequest
    '''
    header_text = header_text.strip().split('\n')
    myheader = {x.split(':')[0] : x.split(':')[1].strip() for x in header_text}
    myheader['Cookie'] = "OUTFOX_SEARCH_USER_ID=-{0}@{1}.{2}.{3}.{4}; ".format(str(random.randint(100000000,999999999)), str(random.randint(10, 241)), str(random.randint(10, 241)), str(random.randint(10, 241)), str(random.randint(10, 241)))
    translate_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    corresponding_data = createData(text_to_trans)

    myheader['Content-Length'] = str(len(corresponding_data))

    # 代理服务器
    proxyHost =
    proxyPort =

    # 代理隧道验证信息
    proxyUser =
    proxyPass =

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    myproxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }

    sess = requests.Session()
    sess.mount('http://', HTTPAdapter(max_retries=5))
    sess.mount('https://', HTTPAdapter(max_retries=5))

    try:
        r = sess.post(translate_url,data=corresponding_data,headers=myheader,proxies=myproxies,timeout=10)
        return r.text
    except requests.exceptions.RequestException as e:
        print(e)
    
