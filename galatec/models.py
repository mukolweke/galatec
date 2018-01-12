from django.db import models


class UserTable(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=120)
    date_reg = models.DateTimeField()