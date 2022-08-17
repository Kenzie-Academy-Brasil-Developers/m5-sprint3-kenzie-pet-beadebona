from django.db import models


# Create your models here.
class Trait (models.Model):
    name = models.CharField(unique=True, max_length=20)
