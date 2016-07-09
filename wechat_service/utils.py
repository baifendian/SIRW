# -*-coding:utf-8-*-

import json
import requests
import logging


def get_token(url):
    try:
        response = requests.get(url)
        result = json.loads(response.content)
    except Exception, e:
        result = {}
        logging.error(e)
    print result.get("access_token", ""), "--------------"
    return result.get("access_token", "")


def generate_menu(url, post_data):
    try:
        post_data = json.dumps(post_data, ensure_ascii=False)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, post_data, headers=headers)
        logging.info(response.content)
        print response.content
    except Exception, e:
        logging.error(e)
