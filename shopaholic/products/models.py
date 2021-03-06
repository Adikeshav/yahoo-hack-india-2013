from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField(default=0, null=True, blank=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Item(TimeStampedModel):
    GENDER_TYPE_CHOICES = (
        ('NA', 'Doesn\'t Matter',),
        ('MALE', 'Male',), ('FEMALE', 'Female',),
        ('BOY', 'Boy',), ('GIRL', 'Girl',),
    )
    name = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    gender_type = models.CharField(max_length=50, choices=GENDER_TYPE_CHOICES)
    url = models.URLField()
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    website = models.ForeignKey(Website)
    slug = models.SlugField()
    image_url1 = models.URLField(null=True, blank=True)
    image_url2 = models.URLField(null=True, blank=True)
    image_url3 = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'