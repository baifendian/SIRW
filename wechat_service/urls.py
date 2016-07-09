#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wechat_index),
    url(r'^set/record/(?P<stock_id>[0-9]+)/$', views.set_stock_record, name='set_record'),
    url(r'^stock/list/$', views.list_stock_info, name='list_stock'),
    url(r'^backtrack/report/$', views.backtrack_report, name='backtrack_report'),
    url(r'^show-history/$', views.show_history_page),
    url(r'^record/data', views.record_data, name='record_data'),
]
