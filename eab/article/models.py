from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, blank=True, max_length=128)