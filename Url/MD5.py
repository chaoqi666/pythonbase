from bs4 import BeautifulSoup as bs
import requests
import hashlib
from urllib.parse import urljoin
import re

def MD5_(md5):
    '''
    url = "https://www.somd5.com/search.php"  # 请求的MD5解密网址
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko'}
    data={
        'hash':md5,               #传入MD5值
        'captcha':'0'
    }

    r = requests.post(url=url, data=data,headers=headers)  # 请求目标网址
    #获取到的返回值
    password=r.content
    #对获取到的值进行相应的UTF8解码
    password=password.decode()
    #将password转化为字典
    password=eval(password)
    #获取密码
    password_final=password['data']
    return password_final
    print(password_final)
    '''
    dict1 = {'0d3bd7b4846b7392':'weihai2009','49ba59abbe56e057':'123456','32aa9ab54b1a8041':'sjzruite',
             'bed8b3f0ae58245f':'yiyue091939','5ed1e780eda39c1b':'521023','f5c047a85e508d6f':'968807',
             'c30fadf5b090edb4':'09912862067','c7c2a92b7d7819fe':' la5332211','da58c2727e476eb3':'hzhf88210381',
             '6e4fb1f592e30ce1':'zrj990802sr'}
    if(md5 in dict1):
        password = dict1.get(md5)
    else:
        password = 'Temporarily unable to decrypt'
    return password


if __name__=="__main__":
    MD5_()

