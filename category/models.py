from django.db import models

# Create your models here.
class Category(models.Model):
    #Behind the scend django will create primarykey column id:BigInt
    name = models.CharField(max_length=50)