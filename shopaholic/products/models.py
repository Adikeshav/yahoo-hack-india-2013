from django.db import models

# Create your models here.

class Websites(models.Model):
    website = models.CharField(max_length=100)
    website_url = models.URLField()