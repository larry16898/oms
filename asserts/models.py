from django.db import models

# Create your models here.
class Asserts(models.Model):
    name = models.CharField(max_length=50,verbose_name='资产名称')
    