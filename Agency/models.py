from django.db import models

# Create your models here.
class AgencyModel(models.Model):
    '''
    代理商表
    '''
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(default="", max_length=100)
    phone   = models.CharField(default="", max_length=25)
    wechat  = models.CharField(default="", max_length=25)
    qq      = models.CharField(default="", max_length=15)
    email   = models.CharField(default="", max_length=50)
    address = models.CharField(default="", max_length=100)


class ProxyModel(models.Model):
    id        = models.AutoField(primary_key=True)
    proxyId   = models.IntegerField(default=0)
    num       = models.IntegerField(default=0)
    unit      = models.CharField(default="", max_length=25)
    productId = models.IntegerField(default=0)
    time      = models.DateField()
    
