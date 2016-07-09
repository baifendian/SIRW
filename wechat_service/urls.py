#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wechat_index),
    url(r'^set/record/$', views.set_stock_record, name='set_record'),
]
