from django.db import models

# Create your models here.


class Websites(models.Model):
    website = models.CharField(max_length=100)
    website_url = models.URLField()

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'


class Brands(models.Model):
    brand = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Categories(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Items(models.Model):
    item = models.CharField(max_length=200)
    item_details = models.TextField(null=True, blank=True)
    item_url = models.URLField()
    category = models.ForeignKey(Categories)
    brand = models.ForeignKey(Brands)
    website = models.ForeignKey(Websites)
    offer_text = models.TextField(null=True, blank=True)
    selling_price = models.FloatField()
    actual_price = models.FloatField(null=True, blank=True)
    discount_rate = models.FloatField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'