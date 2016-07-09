# -*-coding:utf-8-*-

import json
import requests
import logging
import threading
import functools
import time
from wechat.settings_config import DELAY_DAYS

logger = logging.getLogger(__name__)


def get_token(url):
    """get access token from WeChat service

    :param url: request url, WeChat service address
    :return: a json contains access token

    """
    try:
        response = requests.get(url)
        result = json.loads(response.content)
    except Exception, e:
        result = {}
        logger.error(e)
    return result.get("access_token", "")


def generate_menu(url, post_data):
    """post data to WeChat service to generate menu

    :param url: the post url, WeChat service address
    :param post_data: a json contains menu data
    :return: None

    """
    try:
        post_data = json.dumps(post_data, ensure_ascii=False)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, post_data, headers=headers)
        logger.info(response.content)
    except Exception, e:
        logger.error(e)


def async(function):
    """ async methods

    :param function: function's reference
    :return: wrapper

    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        new_thread = threading.Thread(target=function, args=args, kwargs=kwargs)
        new_thread.start()
    return wrapper


@async
def post_message(url, data):
    """post data to url, post message to all the users

    :param url: wechat service url
    :param data: the data that post to wechat service
    :return: None

    """
    try:
        while True:
            time.sleep(3600*24*DELAY_DAYS)
            response = requests.post(url, data, headers={"Content-Type": "application/json"})
            logger.info(response.content)
    except Exception, e:
        logger.error("post message error: %s" % str(e))
