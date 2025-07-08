from django.db import models
import uuid

# Create your models here.
class product(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        editable= False
    )
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length= 1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    return self.name