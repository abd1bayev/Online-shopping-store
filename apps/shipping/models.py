from django.db import models

from apps.checkout.models import ChannelChannel
from apps.product.models import ProductProduct


# Create your models here.


class ShippingShippingzone(models.Model):
    name = models.CharField(max_length=100)
    countries = models.CharField(max_length=749)
    default = models.BooleanField()
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'shipping_shippingzone'



class ShippingShippingmethod(models.Model):
    name = models.CharField(max_length=100)
    maximum_order_weight = models.FloatField(blank=True, null=True)
    minimum_order_weight = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=30)
    shipping_zone = models.ForeignKey(ShippingShippingzone, models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    maximum_delivery_days = models.IntegerField(blank=True, null=True)
    minimum_delivery_days = models.IntegerField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_shippingmethod'


class ShippingShippingmethodExcludedProducts(models.Model):
    shippingmethod = models.ForeignKey(ShippingShippingmethod, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_shippingmethod_excluded_products'
        unique_together = (('shippingmethod', 'product'),)


class ShippingShippingmethodchannellisting(models.Model):
    minimum_order_price_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    currency = models.CharField(max_length=3)
    maximum_order_price_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    price_amount = models.DecimalField(max_digits=12, decimal_places=3)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    shipping_method = models.ForeignKey(ShippingShippingmethod, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_shippingmethodchannellisting'
        unique_together = (('shipping_method', 'channel'),)


class ShippingShippingmethodpostalcoderule(models.Model):
    start = models.CharField(max_length=32)
    end = models.CharField(max_length=32, blank=True, null=True)
    shipping_method = models.ForeignKey(ShippingShippingmethod, models.DO_NOTHING)
    inclusion_type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'shipping_shippingmethodpostalcoderule'
        unique_together = (('shipping_method', 'start', 'end'),)


class ShippingShippingmethodtranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=255, blank=True, null=True)
    shipping_method = models.ForeignKey(ShippingShippingmethod, models.DO_NOTHING)
    description = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_shippingmethodtranslation'
        unique_together = (('language_code', 'shipping_method'),)




class ShippingShippingzoneChannels(models.Model):
    shippingzone = models.ForeignKey(ShippingShippingzone, models.DO_NOTHING)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_shippingzone_channels'
        unique_together = (('shippingzone', 'channel'),)