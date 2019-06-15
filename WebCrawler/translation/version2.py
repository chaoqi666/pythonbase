#延迟提交数据

import urllib.request
import urllib.parse
import json
import time

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
while True:
    content = input("请输入要翻译的内容('q'退出)：")
    if content == 'q':
        break
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15475371556824'
    data['sign'] = 'a864dee6c9bdd010c4de0de1137bd22d'
    data['ts'] = '1547537155682'
    data['bv'] = 'b34b626f1c1da1753c455d5223882b69'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'

    # response提交
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print("翻译的结果是：%s" % (target['translateResult'][0][0]['tgt']))
    #延迟2秒
    time.sleep(2)