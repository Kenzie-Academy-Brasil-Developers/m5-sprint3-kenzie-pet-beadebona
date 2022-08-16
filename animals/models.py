
from django.db import models


# Create your models here.
class Gender(models.TextChoices):
    FEMALE="Fêmea"
    MALE="Macho"
    DEFAULT= "Não informado"

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15,choices=Gender.choices, default=Gender.DEFAULT)
    group = models.ForeignKey("groups.group", on_delete=models.CASCADE, related_name="group_id")
    traits= models.ManyToManyField("traits.trait", related_name="trait")

