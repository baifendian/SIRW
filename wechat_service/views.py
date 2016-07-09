# -*-coding:utf-8-*-
import sys
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from wechat.settings_config import *
from wechat_sdk import WechatConf, WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, EventMessage


conf = WechatConf(
    token=WECHAT_TOKEN,
    appid=WECHAT_APPID,
    appsecret=WECHAT_APPSECRET,
    encrypt_mode=WECHAT_ENCRYPT_MODE
)
wechat = WechatBasic(conf=conf)


@csrf_exempt
def wechat_index(request):
    try:
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
            reply_text_dict = {}
            reply_text = reply_text_dict.get(content, PROMPT_MESSAGE)
            response = wechat.response_text(content=reply_text)
        elif isinstance(message, EventMessage):
            content = message.key
            reply_text_dict = {}
            reply_text = reply_text_dict.get(content, PROMPT_MESSAGE)
            response = wechat.response_text(content=reply_text)
        return HttpResponse(response, content_type="application/xml")
    except Exception, e:
        print sys.exc_info()
        return []





def list_stock_info(request):
    return render(request, "wechat_service/stock_list.html")

def set_stock_record(request, stock_id):
    return render(request, "wechat_service/function.html")

def backtrack_report(request):
    data = [{'data': [['2013-01-01', 13], ['2013-02-01', 15]], 'name': 'input'},
            {'data': [['2013-01-01', 19], ['2013-02-01', 11]], 'name': 'earnings'}]
    return render(request, "wechat_service/datatrack_reports.html", {"data": data})



@require_GET
def show_history_page(request):
    stock_id = request.REQUEST.get("stock")
    return render(request, "wechat_service/show_history.html", {"stock_id": stock_id})
