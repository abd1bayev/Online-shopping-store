from django.db import models

from apps.account.models import AccountUser, AccountAddress
from apps.app.models import AppApp
from apps.checkout.models import ChannelChannel
from apps.discount.models import DiscountVoucher
from apps.giftcard.models import GiftcardGiftcard
from apps.product.models import ProductProductvariant
from apps.shipping.models import ShippingShippingmethod
from apps.sitesettings.models import WarehouseWarehouse, WarehouseStock


# Create your models here.


class OrderOrder(models.Model):
    created = models.DateTimeField()
    tracking_client_id = models.CharField(max_length=36)
    token = models.CharField(unique=True, max_length=36)
    billing_address = models.ForeignKey(AccountAddress, models.DO_NOTHING, blank=True, null=True)
    shipping_address = models.ForeignKey(AccountAddress, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    total_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING, blank=True, null=True)
    language_code = models.CharField(max_length=35)
    shipping_price_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    total_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    shipping_price_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    status = models.CharField(max_length=32)
    shipping_method_name = models.CharField(max_length=255, blank=True, null=True)
    shipping_method = models.ForeignKey(ShippingShippingmethod, models.DO_NOTHING, blank=True, null=True)
    display_gross_prices = models.BooleanField()
    customer_note = models.TextField()
    weight = models.FloatField()
    checkout_token = models.CharField(max_length=36)
    currency = models.CharField(max_length=3)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    redirect_url = models.CharField(max_length=200, blank=True, null=True)
    shipping_tax_rate = models.DecimalField(max_digits=5, decimal_places=4)
    undiscounted_total_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    undiscounted_total_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    total_paid_amount = models.DecimalField(max_digits=12, decimal_places=3)
    origin = models.CharField(max_length=32)
    original = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    collection_point = models.ForeignKey(WarehousWarehouse, models.DO_NOTHING, blank=True, null=True)
    collection_point_name = models.CharField(max_length=255, blank=True, null=True)
    search_document = models.TextField()
    user_phone = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'order_order'



class OrderOrderline(models.Model):
    product_name = models.CharField(max_length=386)
    product_sku = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    unit_price_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    is_shipping_required = models.BooleanField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    quantity_fulfilled = models.IntegerField()
    variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=4)
    translated_product_name = models.CharField(max_length=386)
    currency = models.CharField(max_length=3)
    translated_variant_name = models.CharField(max_length=255)
    variant_name = models.CharField(max_length=255)
    total_price_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    total_price_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    unit_discount_amount = models.DecimalField(max_digits=12, decimal_places=3)
    unit_discount_value = models.DecimalField(max_digits=12, decimal_places=3)
    unit_discount_reason = models.TextField(blank=True, null=True)
    unit_discount_type = models.CharField(max_length=10)
    undiscounted_total_price_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    undiscounted_total_price_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    undiscounted_unit_price_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    undiscounted_unit_price_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    is_gift_card = models.BooleanField()
    product_variant_id = models.CharField(max_length=255, blank=True, null=True)
    sale_id = models.CharField(max_length=255, blank=True, null=True)
    voucher_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_orderline'





class OrderFromUsaSpecialorder(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    status = models.CharField(max_length=32)
    url = models.CharField(max_length=1024)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=560, blank=True, null=True)
    phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'order_from_usa_specialorder'


class OrderFulfillment(models.Model):
    tracking_number = models.CharField(max_length=255)
    created = models.DateTimeField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    fulfillment_order = models.IntegerField()
    status = models.CharField(max_length=32)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    shipping_refund_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    total_refund_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_fulfillment'


class OrderFulfillmentline(models.Model):
    order_line = models.ForeignKey(OrderOrderline, models.DO_NOTHING)
    quantity = models.IntegerField()
    fulfillment = models.ForeignKey(OrderFulfillment, models.DO_NOTHING)
    stock = models.ForeignKey(WarehouseStock, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_fulfillmentline'



class OrderOrderGiftCards(models.Model):
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    giftcard = models.ForeignKey(GiftcardGiftcard, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_order_gift_cards'
        unique_together = (('order', 'giftcard'),)


class OrderOrderevent(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=255)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    parameters = models.JSONField()
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_orderevent'

