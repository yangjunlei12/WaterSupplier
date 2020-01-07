from django.db import models

# Create your models here.

class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=25)

class UserModel(models.Model):
    id            = models.AutoField(primary_key=True)
    open_id       = models.CharField(max_length=50, default="", unique=True)
    name          = models.CharField(max_length=20, default="")
    password      = models.CharField(max_length=16, default="")
    phone         = models.CharField(max_length=11, default="")
    age           = models.IntegerField()
    gender        = models.IntegerField(choices=((0, 'female'), (1, 'male')))
    city          = models.CharField(max_length=20, default="")
    avator        = models.CharField(default="", max_length=50)
    role          = models.ForeignKey(Membership, on_delete=models.CASCADE)
    role_name     = models.CharField(default="", max_length=25)
    end_time      = models.DateField() # 会员结束的时间
    status        = models.IntegerField()
    lastLoginTime = models.DateField()

