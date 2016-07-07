from django.db import models

# Create your models here.

class StockInfo(models.Model):
    name = models.CharField(max_length=1024)
    code = models.CharField(max_length=20)

class StockData(models.Model):
    stock = models.ForeignKey(StockInfo)
    date = models.DateField()
    open_price = models.DecimalField(max_digits=11, decimal_places=3)
    high_price = models.DecimalField(max_digits=11, decimal_places=3)
    close_price = models.DecimalField(max_digits=11, decimal_places=3)
    low_price = models.DecimalField(max_digits=11, decimal_places=3)
    volume = models.IntegerField()
    pe = models.DecimalField(max_digits=6, decimal_places=2)
    pb = models.DecimalField(max_digits=6, decimal_places=2)
    dividend_rate = models.DecimalField(max_digits=5, decimal_places=2)
    index_num = models.DecimalField(max_digits=10, decimal_places=2)


