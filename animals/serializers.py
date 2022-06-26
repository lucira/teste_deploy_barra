from rest_framework import serializers
from animals.models import Animal
from characteristics.models import Characteristic
from groups.models import Groups
from characteristics.serializers import CharacteristicsSerializer
from groups.serializers import GroupsSerializer

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupsSerializer()
    characteristics =  serializers.ListField(child=CharacteristicsSerializer())

    def create(self, validated_data:dict):
         group_data = validated_data.pop("group")
         characteristics_data = validated_data.pop("characteristics")
         print(group_data)
         group,created = Groups.objects.get_or_create(**group_data)
         #push
         characteristics_list = []
         for characteristics in characteristics_data:
             characteristics2,created = Characteristic.objects.get_or_create(**characteristics)
             characteristics_list.append(characteristics2)
         #group = Groups(group_create)
         #characteristics = Characteristic(characteristics_create)

         animal = Animal.objects.create(**validated_data,group=group)
         #set array
         animal.characteristics.set(characteristics_list)
         return animal

