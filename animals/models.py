from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)

    group = models.ForeignKey("groups.Groups",on_delete=models.CASCADE,related_name="animals")
    characteristics = models.ManyToManyField("characteristics.Characteristic",related_name="animals")

    def __repr__(self) -> str:
        return f"Animal {self.id} ({self.name})"
  
   