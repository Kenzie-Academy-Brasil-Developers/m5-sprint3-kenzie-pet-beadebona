
from functools import partial

from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, Response

from animals.models import Animal
from animals.serializers import AnimalSerializer

# Create your views here.

class AnimalView(APIView):
    def get(self, request):
        animals= Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data,200)
    
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, 201)

class AnimalDetailView(APIView):
    def get(self, request, animal_id ):
        animal = get_object_or_404(Animal, id=animal_id)
        serializer = AnimalSerializer(animal)

        return Response(serializer.data, 200)

    def patch(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)

        serializer = AnimalSerializer(animal,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,200)

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)

        animal.delete()

        return Response(status=204)
    ...
