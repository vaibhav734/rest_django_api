from _testcapi import return_null_without_error

from django.db import models

# Create your models here.
class Stock(models.Model):
    ID = 'id'
    TICKER = 'ticker'
    OPEN = 'open'
    CLOSE = 'close'
    VOLUME = 'volume'

    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker

    def to_dict(self):
        res = {
            Stock.ID: self.id,
            Stock.TICKER: self.ticker,
            Stock.OPEN: self.open,
            Stock.CLOSE: self.close,
            Stock.VOLUME: self.volume
        }
        return res