from django.db import models

from products.models import TimeStampModel, Item


class History(TimeStampModel):
    item = models.ForeignKey(Item)
    offer_text = models.TextField(null=True, blank=True)
    selling_price = models.FloatField()
    actual_price = models.FloatField(null=True, blank=True)
    discount_rate = models.FloatField()
    is_offer = models.BooleanField()
    is_in_stock = models.BooleanField()

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Histories"