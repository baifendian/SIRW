# -*-coding:utf-8-*-
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat.settings_config import *
from wechat_sdk import WechatConf, WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage


conf = WechatConf(
    token='test',
    appid='wxa9a580e0ad6fe79e',
    appsecret='8eadd1185e1094108edea040020b1c26',
    encrypt_mode='normal'
)
wechat = WechatBasic(conf=conf)


@csrf_exempt
def wechat_index(request):
    print request
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        if not wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
        return HttpResponse(request.GET.get('echostr', ''), content_type="text/plain")
    try:
        wechat.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
    message = wechat.get_message()
    response = wechat.response_text(content=FOLLOW_MESSAGE)
    if isinstance(message, TextMessage):
        content = message.content.strip().encode("utf-8")
        reply_text_dict = {
            "功能": FUNCTION_MESSAGE,
            "1": STOCK_MESSAGE,
            "2": show_history(),
            "3": show_help(),
        }
        reply_text = reply_text_dict.get(content, PROMPT_MESSAGE)
        response = wechat.response_text(content=reply_text)
    return HttpResponse(response, content_type="application/xml")


def show_help():
    return HELP_MESSAGE


def show_history():
    return "历史"
