# -*-coding:utf-8-*-

FOLLOW_MESSAGE = "Hi~,我是股票推送宝,感谢您的关注！\n回复【功能】两个字查看支持的功能"
FUNCTION_MESSAGE = "1、查看指数\n2、查看投资记录\n3、帮助"  # \n4、选取策略,默认使用【默认策略】(可选功能)
PROMPT_MESSAGE = "回复【功能】两个字查看支持的功能"
STOCK_MESSAGE = "101、<a href=\"http://www.baidu.com\">H股(510900)</a>\n" \
                "102、<a href=\"http://www.xiaomi.com\">恒生(159920)</a>\n" \
                "103、<a href=\"http://www.fuckxiaomi.com\">沪生300(510300)</a>\n" \
                "104、<a href=\"http://www.qq.com\">中证500(510500)</a>\n"
HISTORY_MESSAGE = "201、<a href=\"http://www.duixueqiu.xyz/wechat/stock-history/?stock=510900\" target=\"_blank\">" \
                  "H股(510900)</a>\n" \
                  "202、<a href=\"http://www.duixueqiu.xyz/wechat/stock-history/?stock=159920\" target=\"_blank\">" \
                  "恒生(159920)</a>\n" \
                  "203、<a href=\"http://www.duixueqiu.xyz/wechat/stock-history/?stock=510300\" target=\"_blank\">" \
                  "沪生300(510300)</a>\n" \
                  "204、<a href=\"http://www.duixueqiu.xyz/wechat/stock-history/?stock=510500\" target=\"_blank\">" \
                  "中证500(510500)</a>\n"
HELP_MESSAGE = "显示关于定投的优势,策略信息等!"

# for wechat
WECHAT_TOKEN = "test"
WECHAT_APPID = "wxa9a580e0ad6fe79e"
WECHAT_APPSECRET = "8eadd1185e1094108edea040020b1c26"
WECHAT_ENCRYPT_MODE = "normal"
ACCESS_TOKEN_REQUEST_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential" \
                           "&appid=%s" \
                           "&secret=%s" % (WECHAT_APPID, WECHAT_APPSECRET)
GENERATE_MENU_URL = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s"
GENERATE_MENU_DATA = {
    "button": [
        {
            "type": "view",
            "name": "查看指数",
            "url": "http://www.duixueqiu.xyz/wechat/stock-history/?stock=159920"
        },
        {
            "type": "view",
            "name": "查看记录",
            "url": "http://www.duixueqiu.xyz/wechat/stock-history/?stock=510300"
        },
        {
            "type": "click",
            "name": "帮助",
            "key": "功能"
        }
    ]
}
