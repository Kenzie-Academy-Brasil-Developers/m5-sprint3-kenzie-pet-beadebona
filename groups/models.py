from django.db import models

# Create your models here.

class Group (models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50, unique=True)
