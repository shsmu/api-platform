# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        db_table = 'alembic_version'

class Project(models.Model):
    projectid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)

    # If the field is a ForeignKey,
    # Django will display the str() (unicode() on Python 2) of the related object.
    # If you don’t set list_display,
    # the admin site will display a single column that displays the str() (unicode() on Python 2) representation of each object.

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'

class Api(models.Model):
    name = models.CharField('接口名称', max_length=32, blank=True, null=True)
    uri = models.CharField(max_length=128, blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    contenttype = models.CharField('Content-Type', max_length=64, blank=True, null=True)
    charset = models.CharField('字符集', max_length=32, blank=True, null=True)
    reqdata = models.TextField(blank=True, null=True)
    respdata = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('User', db_column='userid', blank=True, null=True)
    createdtime = models.DateTimeField(blank=True, null=True)
    chk_field = models.CharField('检测项', max_length=32, blank=True, null=True)
    expect_rst = models.CharField('预期值', max_length=10, blank=True, null=True)
    timeout = models.CharField('超时时间', max_length=10, blank=True, null=True)
    projectid = models.ForeignKey('project', db_column='projectid', blank=True, null=True)

    class Meta:
        verbose_name = "API"
        db_table = 'api'


class ApiCase(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    apiid = models.ForeignKey(Api, db_column='apiid', blank=True, null=True)
    userid = models.ForeignKey('User', db_column='userid', blank=True, null=True)

    class Meta:
        db_table = 'api_case'


class TestSuit(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    orders = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('User', db_column='userid', blank=True, null=True)
    createdtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'test_suit'


class User(models.Model):
    nickname = models.CharField(max_length=32, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    phonenum = models.CharField(unique=True, max_length=32, blank=True, null=True)
    email = models.CharField(unique=True, max_length=32, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    password_heihei = models.CharField(max_length=2048, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    createdtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user'
