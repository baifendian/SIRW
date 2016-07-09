from django.db import models

# Create your models here.


class StockInfo(models.Model):
    name = models.CharField(max_length=1024)
    code = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    pe = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

class StockData(models.Model):
    stock = models.ForeignKey(StockInfo)
    date = models.DateField()
    open_price = models.DecimalField(max_digits=11, decimal_places=3, null=True, blank=True)
    high_price = models.DecimalField(max_digits=11, decimal_places=3, null=True, blank=True)
    close_price = models.DecimalField(max_digits=11, decimal_places=3)
    low_price = models.DecimalField(max_digits=11, decimal_places=3, null=True, blank=True)
    volume = models.IntegerField(blank=True, null=True)
    pe = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    pb = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    dividend_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    index_num = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class UserInfo(models.Model):
    user_id = models.CharField(max_length=50)
    join_date = models.DateField()
    is_active = models.BooleanField(True)

class UserStockRecord(models.Model):
    user = models.ForeignKey(UserInfo)
    date = models.DateField()
    current_price = models.IntegerField()
    market_value = models.IntegerField()
    sum_total = models.IntegerField()
    sum_profit = models.IntegerField()
    profit_ratio = models.DecimalField(max_digits=6, decimal_places=2)
    cash = models.IntegerField()
    pre_cal_value = models.IntegerField(null=True, blank=True)



