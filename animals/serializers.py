from rest_framework import serializers

from animals.models import Gender


class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=Gender.choices, default= Gender.DEFAULT)
