from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=20,unique=True)
    scientific_name = models.CharField(max_length=50,unique=True)


    def __repr__(self) -> str:
        return f"Groups {self.id} ({self.name})"

