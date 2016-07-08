#!/usr/bin/env python
# encoding: utf-8

from django import forms

class SetRecordForm(forms.Form):
    base_price = forms.FloatField(required=True)
    growth_factor = forms.FloatField(required=True)
