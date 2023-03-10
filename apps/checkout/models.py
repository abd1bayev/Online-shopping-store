from django.db import models
from apps.account.models import AccountUser, AccountAddress
from apps.giftcard.models import GiftcardGiftcard
from apps.product.models import ProductProductvariant
from apps.shipping.models import ShippingShippingmethod
from apps.sitesettings.models import WarehouseWarehouse


# Create your models here.

class ChannelChannel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=255)
    is_active = models.BooleanField()
    currency_code = models.CharField(max_length=3)
    default_country = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'channel_channel'


class PluginsPluginconfiguration(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    active = models.BooleanField()
    configuration = models.JSONField(blank=True, null=True)
    identifier = models.CharField(max_length=128)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugins_pluginconfiguration'
        unique_together = (('identifier', 'channel'),)


class PluginsEmailtemplate(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    plugin_configuration = models.ForeignKey(PluginsPluginconfiguration, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'plugins_emailtemplate'





class CheckoutCheckout(models.Model):
    created = models.DateTimeField()
    last_change = models.DateTimeField()
    token = models.UUIDField(primary_key=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    billing_address = models.ForeignKey(AccountAddress, models.DO_NOTHING, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=3)
    discount_name = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField()
    shipping_address = models.ForeignKey(AccountAddress, models.DO_NOTHING, blank=True, null=True)
    shipping_method = models.ForeignKey(ShippingShippingmethod, models.DO_NOTHING, blank=True, null=True)
    voucher_code = models.CharField(max_length=12, blank=True, null=True)
    translated_discount_name = models.CharField(max_length=255, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    currency = models.CharField(max_length=3)
    country = models.CharField(max_length=2)
    redirect_url = models.CharField(max_length=200, blank=True, null=True)
    tracking_code = models.CharField(max_length=255, blank=True, null=True)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    language_code = models.CharField(max_length=35)
    collection_point = models.ForeignKey(WarehouseWarehouse, models.DO_NOTHING, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkout_checkout'


class CheckoutCheckoutGiftCards(models.Model):
    checkout = models.ForeignKey(CheckoutCheckout, models.DO_NOTHING)
    giftcard = models.ForeignKey(GiftcardGiftcard, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'checkout_checkout_gift_cards'
        unique_together = (('checkout', 'giftcard'),)


class CheckoutCheckoutline(models.Model):
    quantity = models.IntegerField()
    checkout = models.ForeignKey(CheckoutCheckout, models.DO_NOTHING)
    variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'checkout_checkoutline'