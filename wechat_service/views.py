# -*-coding:utf-8-*-
import datetime
import sys
import logging
import json
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.core.cache import cache
from wechat.settings_config import *
from wechat_sdk import WechatConf, WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, EventMessage
from .models import StockData, StockInfo, UserInfo, UserStockRecord
from resource.Compute import Compute

# this is logger
logger = logging.getLogger('access_log')


conf = WechatConf(
    token=WECHAT_TOKEN,
    appid=WECHAT_APPID,
    appsecret=WECHAT_APPSECRET,
    encrypt_mode=WECHAT_ENCRYPT_MODE
)
wechat = WechatBasic(conf=conf)


@csrf_exempt
def wechat_index(request):
    """WeChat interface, most logic in this method

    :param request: the request from WeChat mobile client
    :return: XML response

    """
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
            logger.error("wechat parse data error!")
            return HttpResponseBadRequest('Invalid XML Data')
        message = wechat.get_message()
        response = wechat.response_text(content=FOLLOW_MESSAGE)
        reply_text_dict = {
            "功能": FUNCTION_MESSAGE,
            "3+1": POWER_INTRODUCTION,
            "3+2": RECORD_INTRODUCTION
        }
        if isinstance(message, TextMessage):
            content = message.content.strip().encode("utf-8")
            reply_text = reply_text_dict.get(content, PROMPT_MESSAGE)
            response = wechat.response_text(content=reply_text)
        elif isinstance(message, EventMessage):
            content = message.key
            reply_text = reply_text_dict.get(content, PROMPT_MESSAGE)
            response = wechat.response_text(content=reply_text)
        return HttpResponse(response, content_type="application/xml")
    except Exception, e:
        logger.error(sys.exc_info())
        logger.error("wechat index error: %s" % str(e))
        return []


def list_stock_info(request):
    return render(request, "wechat_service/stock_list.html")

def set_stock_record(request, stock_id):
    return render(request, "wechat_service/function.html", {"stock_id": stock_id})

def backtrack_report(request):
    data = cache.get('return_data')
    return render(request, "wechat_service/datatrack_reports.html", {"data": data})

@csrf_exempt
def record_data(request):
    try:
        start_day = request.GET.get('start_day')
        end_day = request.GET.get('end_day')
        initial_price = int(float(request.GET.get('qishijine2')))
        growth_factor = float(request.GET.get('zengzhangxishu2'))
        stock_id = request.GET.get('stock_id')
        stock_model = StockInfo.objects.get(code=stock_id)
        start_day = datetime.datetime.strptime(start_day, '%Y-%m-%d').date()
        if start_day < stock_model.date:
            start_day = stock_model.date
        end_day = datetime.datetime.strptime(end_day, '%Y-%m-%d').date()
        if end_day > datetime.date.today():
            end_day = datetime.date.today()
        if initial_price < 100 or initial_price >= 1000000:
            initial_price = 2000
        if growth_factor < 0.01 or growth_factor >= 1:
            growth_factor = 0.01
        cur = stock_model.stockdata_set.filter(date__lte=end_day, date__gte=start_day).order_by('date')
        if cur:
            price_list = []
            price_date = []
            current_date = cur[0].date
            for elem in cur:
                if current_date <= elem.date:
                    price_date.append(elem.date.strftime('%Y-%m-%d'))
                    price_list.append(elem.close_price)
                    #如何更好的找到下一个月的今天的前后几天？
                    current_date += datetime.timedelta(days=28)
            compute = Compute()
            results = compute.backTest(price_list, initial_price, 5 * initial_price, growth_factor, 0)
            return_data = [{'data': [], 'name': 'month_input'},
                           {'data': [], 'name': 'total_input'},
                           {'data': [], 'name': 'total_value'},
                           {'data': [], 'name': 'total_sell'},
                           ]
            for index in range(len(price_date)):
                return_data[0]['data'].append([price_date[index], results[index][0]])
                return_data[1]['data'].append([price_date[index], results[index][2]])
                return_data[2]['data'].append([price_date[index], results[index][1]+results[index][5]])
                return_data[3]['data'].append([price_date[index], results[index][5]])
            #logger.debug(return_data)
            cache.set('return_data', return_data, 30)
            return HttpResponse(json.dumps({'status': 'ok'}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'status': 'no result'}), content_type="application/json")
    except Exception as e:
        #logger.debug(sys.exc_info())
        logger.exception(e)
        return HttpResponse(json.dumps({'status': 'error'}), content_type="application/json")


