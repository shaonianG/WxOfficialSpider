# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import random,re
from fake_useragent import UserAgent

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

begin = "0"
token = ""
#需要从微信公众平台获取
fakeid = ""
#需要从微信公众平台获取
cookie_str = ""
#需要从微信公众平台获取

params = {
    "action": "list_ex",
    "begin": begin,
    "count": "5",
    "fakeid": fakeid,
    "type": "9",
    "token": token,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1"
}


import requests

def main():
    print("开始抓取")
    while(True):
        index = 0
        result = getInfo(index)
        while(len(result['app_msg_list'])):
            index += 1
            getInfo(index)
            if (result['base_resp']['ret'] == 200040):
                getInfo(index)
        print("睡眠一天")
        time.sleep(86400)


def getInfo(begin):
    ua = UserAgent(path='./fake_useragent.json')
    # ua代理
    headers = {
        "Cookie": cookie_str,
        "User-Agent": ua.random
    }

    #参数begin
    params["begin"] = str(begin * 5)
    #随机暂停
    random_sleep(5, 10)
    result = requests.get(url, headers=headers, verify=False,params = params,).json()
    try:
        app_msg_list = result['app_msg_list']

        for item in app_msg_list:
            print(item["digest"])
            print(item["title"])
    except:
        if(result['base_resp']['ret'] == 200040):
            print(result['base_resp']['ret'])
            print(result['base_resp']['err_msg'])
            print("token过期，更换token")
            params['token'] = getToken()

    return result

def getToken():

    ua = UserAgent(path='./fake_useragent.json')
    cookies = {}
    s = requests.Session()
    url = 'https://mp.weixin.qq.com'

    headers = {
        'User-Agent': ua.random,
        "Host": "mp.weixin.qq.com",
        'Referer': 'https://mp.weixin.qq.com/'
    }

    for item in cookie_str.split(';'):
        sep_index = item.find('=')
        cookies[item[:sep_index]] = item[sep_index + 1:]

    res = s.get(url=url, headers=headers, cookies=cookies, verify=False)
    if res.status_code == 200:
        print(res.url)
        token = re.findall(r'.*?token=(\d+)', res.url)
        if token:
            token = token[0]
        else:
            print('登陆失败')

    return token

#随机休眠
def random_sleep(start, end):
    # 随机暂停若干时间，暂停时间介于start和end之间
    t = random.uniform(start,end)
    time.sleep(t)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/