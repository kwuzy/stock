from django.db import models

# Create your models here.

class Stocks(models.Model):
    ticker = models.CharField(max_length = 100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)