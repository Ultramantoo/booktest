from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()


"""
类名：HeroInfo
英雄姓名：hname
英雄性别：hgender
英雄简介：hcomment
英雄所属图书：hbook
图书-英雄的关系为一对多
"""


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)