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
        
         group,created = Groups.objects.get_or_create(**group_data)

         characteristics_list = []
         for characteristics in characteristics_data:
             characteristics2,created = Characteristic.objects.get_or_create(**characteristics)
             characteristics_list.append(characteristics2)

         animal = Animal.objects.create(**validated_data,group=group)
         animal.characteristics.set(characteristics_list)
         return animal

    def update(self, instance:Animal, validated_data:dict):

        non_editable_keys = ("sex","group")
        for key,value in validated_data.items():
            if key in non_editable_keys:
                raise KeyError
            setattr(instance,key,value)
       
        instance.save()
        return instance     

