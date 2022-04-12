# WxOfficialSpider
python半自动爬取微信公众号文章列表，需要注册微信公众号账户

其中fakeid，cookies和token需要手动登录微信公众平台获取

fakeid是固定的，cookies和token每次登出后都会改变，需要重新手动设置

token会失效，可以凭借cookies再次获取

安装faker-useragent

```pip install fake-useragent```

##获取参数教程

登录后台后，点击新的创作

![image-20220412205528349](https://tva1.sinaimg.cn/large/e6c9d24ely1h179p7o7eaj21l50u0adl.jpg)

进入后点击超链接

![image-20220412205647339](https://tva1.sinaimg.cn/large/e6c9d24ely1h179pcrulqj21jf0u0q4y.jpg)

选择其他公众号

![image-20220412205713902](https://tva1.sinaimg.cn/large/e6c9d24ely1h179pexmb7j20za0n6q4e.jpg)

搜索想要爬取的公众号（先不要点击），打开浏览器f12，network界面

![image-20220412205750023](https://tva1.sinaimg.cn/large/e6c9d24ely1h179pia8d5j20to0fyjsd.jpg)

![image-20220412205851182](https://tva1.sinaimg.cn/large/e6c9d24ely1h179pkjh31j20ns0s8761.jpg)

点击公众号

然后network里面就会出现一个请求，翻到request header这里

![image-20220412210043311](https://tva1.sinaimg.cn/large/e6c9d24ely1h179u6yrz4j20n00g8abe.jpg)

所需要的cookies在这里获取

![image-20220412210116226](https://tva1.sinaimg.cn/large/e6c9d24ely1h179up4n4kj20n80iatbf.jpg)

然后点击payload，token和fakeid在这里获取

![image-20220412210211393](https://tva1.sinaimg.cn/large/e6c9d24ely1h179venci1j20na0higmg.jpg)
