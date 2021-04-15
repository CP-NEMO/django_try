from django.db import models

class Databse(models.Model):
    Condition = models.CharField(max_length= 30)
    Date = models.CharField(max_length=12)