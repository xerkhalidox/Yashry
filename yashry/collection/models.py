from django.db import models
SIZE_CHOICES = [
    ('S', "Small"),
    ('M', "Medium"),
    ('L', "Large")
]
GENDER = [
    ('M', "Male"),
    ('F', "Female")
]


class Product(models.Model):
    category = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=2)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    size = models.CharField(choices=SIZE_CHOICES, max_length=3)
    color = models.CharField(max_length=10)
