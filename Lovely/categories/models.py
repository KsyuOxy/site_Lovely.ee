from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150)
    about = models.TextField(max_length=2048)
    max_products = models.IntegerField(default=20)  # для тренировки
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
