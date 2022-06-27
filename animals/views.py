from django.shortcuts import get_object_or_404
from rest_framework.views import APIView,status
from rest_framework.response import Response
from django.core import serializers
from .models import Animal
from .serializers import AnimalSerializer


class AnimalView(APIView):

    def patch(self,request,animal_id=None):
        if animal_id:
            animal = get_object_or_404(Animal,pk=animal_id)
            serializer = AnimalSerializer(animal,request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            try:
              serializer.save()
            except KeyError:
              return Response({"error":"Náo pode atualizar"},status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data)

    def delete(self,request,animal_id=None):
        if animal_id:
            animal = get_object_or_404(Animal,pk=animal_id)
            animal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self,request,animal_id=None):

        if animal_id:
            animal = Animal.objects.get(pk=animal_id)
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
       

        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals,many=True)
 

        return Response(serializer.data)

    def post(self,request):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
  
        serializer.save()
        return Response(serializer.data)    
