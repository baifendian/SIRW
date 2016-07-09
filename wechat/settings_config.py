# -*-coding:utf-8-*-

FOLLOW_MESSAGE = "Hi~,我是股票推送宝,感谢您的关注！\n回复【功能】两个字查看支持的功能"
FUNCTION_MESSAGE = "1、查看指数\n2、查看投资记录\n3、帮助\n" \
                   "提示:\n" \
                   "输入: \"3+1\"查看指数的功能简介\n" \
                   "输入: \"3+2\"查看投资记录的功能简介\n"
POWER_INTRODUCTION = "点击菜单栏中\"查看指数\"按钮,显示相关股票的指数信息,\n并选择\"回测\"或是\"定投\"进行相关操作,\n完成操作。"
RECORD_INTRODUCTION = "点击菜单栏中\"查看记录\"按钮,显示相关股票的历史信息,\n并可以进行\"查看历史\"或进行\"买入\"操作。"
PROMPT_MESSAGE = "回复【功能】两个字查看支持的功能"

# for wechat
WECHAT_TOKEN = "test"
WECHAT_APPID = "wxa9a580e0ad6fe79e"
WECHAT_APPSECRET = "8eadd1185e1094108edea040020b1c26"
WECHAT_ENCRYPT_MODE = "normal"
ACCESS_TOKEN_REQUEST_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential" \
                           "&appid=%s" \
                           "&secret=%s" % (WECHAT_APPID, WECHAT_APPSECRET)
POST_MESSAGE_URL = "https://api.weixin.qq.com/cgi-bin/media/uploadnews?access_token=%s"
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
