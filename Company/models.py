from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    id            = models.AutoField(primary_key=True)
    name          = models.CharField(default="", max_length=50)
    logo          = models.CharField(default="", max_length=50)
    member_status = models.IntegerField(default=0)
    phone         = models.CharField(default="", max_length=25)
    wechat        = models.CharField(default="", max_length=25)
    qq            = models.CharField(default="", max_length=15)
    email         = models.CharField(default="", max_length=50)
    address       = models.CharField(default="", max_length=100)

class ArticleModel(models.Model):
    id            = models.AutoField(primary_key=True)
    company_id    = models.IntegerField(default=0)
    ### True是动态 False 是活动
    type          = models.BooleanField(choices=((True, 'news'), (False, 'activity')))
    content       = models.CharField(default="", max_length=500)
    title         = models.CharField(default="", max_length=200)
    abstract      = models.CharField(default="", max_length=250)
    images        = models.CharField(default="", max_length=500)
    status        = models.BooleanField() 
    create_time   = models.DateField()
    visits        = models.IntegerField(default=0)
    likes         = models.IntegerField(default=0)
    shares        = models.IntegerField(default=0)
    member_status = models.IntegerField(default=0)
