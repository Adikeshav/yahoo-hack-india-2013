from django.db import models

from products.models import Category, Brand
# Create your models here.


class UserInterest(models.Model):
    GENDER_TYPE_CHOICES = (
        ('NA', 'Doesn\'t Matter',),
        ('MALE', 'Male',), ('FEMALE', 'Female',),
        ('BOY', 'Boy',), ('GIRL', 'Girl',),
    )
    email = models.EmailField(blank=True)
    interest = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    gender_type = models.CharField(max_length=50, choices=GENDER_TYPE_CHOICES)