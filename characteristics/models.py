from django.db import models

class Characteristic(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __repr__(self) -> str:
        return f"Characteristics {self.id} ({self.name})"
