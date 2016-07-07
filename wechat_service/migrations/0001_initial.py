# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('open_price', models.DecimalField(max_digits=11, decimal_places=3)),
                ('high_price', models.DecimalField(max_digits=11, decimal_places=3)),
                ('close_price', models.DecimalField(max_digits=11, decimal_places=3)),
                ('low_price', models.DecimalField(max_digits=11, decimal_places=3)),
                ('volume', models.IntegerField()),
                ('pe', models.DecimalField(max_digits=6, decimal_places=2)),
                ('pb', models.DecimalField(max_digits=6, decimal_places=2)),
                ('dividend_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('index_num', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock',
            field=models.ForeignKey(to='wechat_service.StockInfo'),
        ),
    ]
