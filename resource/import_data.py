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

def from_csv_to_db(filename='510900.csv', stock_name=u'H股ETF', stock_code='510900'):
    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        first_row = True
        stock_model = StockInfo(name=stock_name, code=stock_code, date=datetime.date(2013, 3, 21))
        stock_model.save()
        for row in spamreader:
            if first_row:
                first_row = False
                continue

            stock_data_model = StockData(stock=stock_model, date=datetime.datetime.strptime(row[0], '%Y-%m-%d'), open_price=float(row[1]),
                                        high_price=float(row[2]), low_price=float(row[3]), close_price=float(row[4]), volume=float(row[5]))
            stock_data_model.save()


if __name__ == '__main__':
    from_csv_to_db()




