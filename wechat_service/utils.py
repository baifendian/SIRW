# -*-coding:utf-8-*-

import json
import requests
import logging

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


def post_message(url):
    """post data to user

    :param url: post url
    :return: None

    """
