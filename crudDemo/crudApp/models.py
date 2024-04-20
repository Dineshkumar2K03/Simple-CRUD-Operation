from django.db import models

class student(models.Model):
    sno       = models.IntegerField()
    sname     = models.CharField(max_length=30)
    sclass    = models.IntegerField()
    saddress  = models.CharField(max_length=100)

