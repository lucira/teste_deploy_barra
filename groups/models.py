from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=20)
    scientific_name = models.CharField(max_length=50)


    def __repr__(self) -> str:
        return f"Groups {self.id} ({self.name})"

