#!/usr/bin/env python
# encoding: utf-8

import datetime
import os
import sys
import django
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wechat.settings")
django.setup()

from wechat_service.models import StockInfo, StockData

def from_csv_to_db(filename='159915.csv', stock_name=u'创业板', stock_code='159915'):
    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        first_row = True
        stock_model = StockInfo(stock_name, stock_code)
        stock_model.save()
        for row in spamreader:
            if first_row:
                first_row = False
                continue
            stock_data_model = StockData(stock=stock_model, data=datetime.datetime.strptime(row[0], '%Y-%m-%d'), open_price=row[1],
                                        high_price=row[2], low_price=row[3], close_price=row[4], volume=row[5])
            stock_data_model.save()


if __name__ == '__main__':
    from_csv_to_db()




