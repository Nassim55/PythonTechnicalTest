from django.conf import settings
from django.db import models


class Bond(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isin = models.CharField(max_length=100)
    size = models.BigIntegerField()
    currency = models.CharField(max_length=3)
    maturity = models.CharField(max_length=10)
    lei = models.CharField(max_length=100)