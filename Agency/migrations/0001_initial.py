# Generated by Django 2.2 on 2019-11-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=25)),
                ('wechat', models.CharField(default='', max_length=25)),
                ('qq', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proxyId', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
                ('unit', models.CharField(default='', max_length=25)),
                ('productId', models.IntegerField(default=0)),
                ('time', models.DateField()),
            ],
        ),
    ]