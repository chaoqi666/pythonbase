#IP代理

import urllib.request
import urllib.parse
import json


content = input("请输入要翻译的内容：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

#ip代理
proxy_support = urllib.request.ProxyHandler({'http':'112.91.218.21:9000'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')]
urllib.request.install_opener(opener)

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

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
target = json.loads(html)
print("翻译的结果是：%s" % (target['translateResult'][0][0]['tgt']))
print("使用IP为:112.91.218.21")
