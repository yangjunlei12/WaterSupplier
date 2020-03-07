from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id         = models.AutoField(primary_key=True)
    company_id = models.IntegerField(default=0)
    type_id    = models.IntegerField(default=0)
    title      = models.CharField(null=False, max_length=30)
    images     = models.CharField(default="", max_length=500)
    abstract   = models.CharField(default="", max_length=100)
    content    = models.CharField(default="", max_length=200)
    like       = models.IntegerField(default=0)
    share      = models.IntegerField(default=0)
    cultureId  = models.IntegerField(default=0)
    sales      = models.IntegerField(default=0)
    quantity   = models.FloatField(default=0.0)
    price      = models.FloatField(default=0.0)
    discount   = models.FloatField(default=0.0)
    create     = models.DateField(auto_now=True)
    
class ProductType(models.Model):
    id   = models.AutoField(primary_key=True)
    company_id = models.IntegerField(default=0)
    name = models.CharField(default="", max_length=100)