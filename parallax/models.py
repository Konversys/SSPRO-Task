from django.db import models

class Direction(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    fromx = models.CharField(max_length=32)
    tox = models.CharField(max_length=32)
    uid = models.CharField(max_length=32)
    date = models.DateTimeField()

class Count(models.Model):
    count = models.AutoField(primary_key=True)