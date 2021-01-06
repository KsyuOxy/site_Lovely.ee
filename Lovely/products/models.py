from django.db import models
from categories.models import Categories


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=155)
    about = models.TextField(max_length=2048)
    expiration_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
