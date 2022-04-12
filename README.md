# WxOfficialSpider
python半自动爬取微信公众号文章列表，需要注册微信公众号账户

其中fakeid，cookies和token需要手动登录微信公众平台获取

fakeid是固定的，cookies和token每次登出后都会改变，需要重新手动设置

token会失效，可以凭借cookies再次获取

安装faker-useragent

```pip install fake-useragent```
##获取参数教程

登录后台后，点击新的创作

![image-20220412205528349](/Users/shaonian/Library/Application Support/typora-user-images/image-20220412205528349.png)

进入后点击超链接

![image-20220412205647339](/Users/shaonian/Library/Application Support/typora-user-images/image-20220412205647339.png)

选择其他公众号

![image-20220412205713902](/Users/shaonian/Library/Application Support/typora-user-images/image-20220412205713902.png)

搜索想要爬取的公众号（先不要点击），打开浏览器f12，network界面

![image-20220412205750023](/Users/shaonian/Library/Application Support/typora-user-images/image-20220412205750023.png)

![image-20220412205851182](/Users/shaonian/Library/Application Support/typora-user-images/image-20220412205851182.png)

点击公众号
