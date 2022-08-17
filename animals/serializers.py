import math

from groups.models import Group
from groups.serializers import GroupSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from traits.models import Trait
from traits.serializers import TraitSerializer

from animals.models import Animal, Gender


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=Gender.choices, default= Gender.DEFAULT)

    traits = TraitSerializer(many=True)
    group = GroupSerializer()
    human_age = serializers.SerializerMethodField()

    def get_human_age(self, obj: Animal) -> str:
        return 16 * math.log1p(obj.age) + 31

    def create(self, validated_data):
        traits = validated_data.pop("traits")
        group = validated_data.pop("group")

        group,_ = Group.objects.get_or_create(**group)

        animal = Animal.objects.create(**validated_data, group=group)

        if traits:
            for trait_data in traits:
                trait,_ = Trait.objects.get_or_create(**trait_data)

                animal.traits.add(trait)

        animal.save()
        return animal
    def update(self, instance, validated_data):
        immutable_key = ("traits", "group" , "sex")

        errors = {}

        for field, value in validated_data.items():
            if field in immutable_key:
                errors.update({f"{field}": f"You can not update {field} property."})
                continue

            setattr(instance, field, value)

        if errors:
            raise ValidationError(errors)

        instance.save()

        return instance
