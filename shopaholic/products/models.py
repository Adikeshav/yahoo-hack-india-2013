from django.db import models

# Create your models here.


<<<<<<< HEAD
class Website(models.Model):
    website = models.CharField(max_length=100)
    website_url = models.URLField()
    slug = models.SlugField()
=======
class Websites(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
>>>>>>> fe38768b4fcc89bc25ab20b62df0724f6d6d792d

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField(default=0, null=True, blank=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Item(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    url = models.URLField()
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    website = models.ForeignKey(Website)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'