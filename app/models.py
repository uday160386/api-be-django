from django.db import models


# Create your models here.
class Medicines(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    qty = models.IntegerField(default=1)
