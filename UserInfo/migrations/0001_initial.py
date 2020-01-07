# Generated by Django 2.2 on 2019-11-11 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('open_id', models.CharField(default='', max_length=50, unique=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=16)),
                ('phone', models.CharField(default='', max_length=11)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'female'), (1, 'male')])),
                ('city', models.CharField(default='', max_length=20)),
                ('avator', models.CharField(default='', max_length=50)),
                ('role_name', models.CharField(default='', max_length=25)),
                ('end_time', models.DateField()),
                ('status', models.IntegerField()),
                ('lastLoginTime', models.DateField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserInfo.Membership')),
            ],
        ),
    ]
