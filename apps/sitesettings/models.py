from django.db import models
from django.contrib.sites.models import Site

from apps.account.models import AccountAddress
from apps.app.models import AppApp
from apps.checkout.models import CheckoutCheckoutline
from apps.menu.models import MenuMenu
from apps.order.models import OrderOrderline
from apps.product.models import ProductProductvariantchannellisting, ProductProductvariant
from apps.shipping.models import ShippingShippingzone


# Create your models here.


class SiteSitesettings(models.Model):
    header_text = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    site = models.OneToOneField(Site, models.DO_NOTHING)
    bottom_menu = models.ForeignKey(MenuMenu, models.DO_NOTHING, blank=True, null=True)
    top_menu = models.ForeignKey(MenuMenu, models.DO_NOTHING, blank=True, null=True)
    display_gross_prices = models.BooleanField()
    include_taxes_in_prices = models.BooleanField()
    charge_taxes_on_shipping = models.BooleanField()
    track_inventory_by_default = models.BooleanField()
    default_weight_unit = models.CharField(max_length=30)
    automatic_fulfillment_digital_products = models.BooleanField()
    default_digital_max_downloads = models.IntegerField(blank=True, null=True)
    default_digital_url_valid_days = models.IntegerField(blank=True, null=True)
    company_address = models.ForeignKey(AccountAddress, models.DO_NOTHING, blank=True, null=True)
    default_mail_sender_address = models.CharField(max_length=254, blank=True, null=True)
    default_mail_sender_name = models.CharField(max_length=78)
    customer_set_password_url = models.CharField(max_length=255, blank=True, null=True)
    automatically_confirm_all_new_orders = models.BooleanField()
    fulfillment_allow_unpaid = models.BooleanField()
    fulfillment_auto_approve = models.BooleanField()
    automatically_fulfill_non_shippable_gift_card = models.BooleanField()
    gift_card_expiry_period = models.IntegerField(blank=True, null=True)
    gift_card_expiry_period_type = models.CharField(max_length=32, blank=True, null=True)
    gift_card_expiry_type = models.CharField(max_length=32)
    reserve_stock_duration_anonymous_user = models.IntegerField(blank=True, null=True)
    reserve_stock_duration_authenticated_user = models.IntegerField(blank=True, null=True)
    limit_quantity_per_checkout = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_sitesettings'


class SiteSitesettingstranslation(models.Model):
    language_code = models.CharField(max_length=35)
    header_text = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    site_settings = models.ForeignKey(SiteSitesettings, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'site_sitesettingstranslation'
        unique_together = (('language_code', 'site_settings'),)



class WarehouseWarehouse(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=250)
    address = models.ForeignKey(AccountAddress, models.DO_NOTHING)
    slug = models.CharField(unique=True, max_length=255)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    click_and_collect_option = models.CharField(max_length=30)
    is_private = models.BooleanField()
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'warehouse_warehouse'


class WarehouseStock(models.Model):
    quantity = models.IntegerField()
    product_variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)
    warehouse = models.ForeignKey(WarehouseWarehouse, models.DO_NOTHING)
    quantity_allocated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'warehouse_stock'
        unique_together = (('warehouse', 'product_variant'),)



class WarehouseAllocation(models.Model):
    quantity_allocated = models.IntegerField()
    order_line = models.ForeignKey(OrderOrderline, models.DO_NOTHING)
    stock = models.ForeignKey(WarehouseStock, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_allocation'
        unique_together = (('order_line', 'stock'),)


class WarehousePreorderallocation(models.Model):
    quantity = models.IntegerField()
    order_line = models.ForeignKey(OrderOrderline, models.DO_NOTHING)
    product_variant_channel_listing = models.ForeignKey(ProductProductvariantchannellisting, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_preorderallocation'
        unique_together = (('order_line', 'product_variant_channel_listing'),)


class WarehousePreorderreservation(models.Model):
    quantity_reserved = models.IntegerField()
    reserved_until = models.DateTimeField()
    checkout_line = models.ForeignKey(CheckoutCheckoutline, models.DO_NOTHING)
    product_variant_channel_listing = models.ForeignKey(ProductProductvariantchannellisting, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_preorderreservation'
        unique_together = (('checkout_line', 'product_variant_channel_listing'),)


class WarehouseReservation(models.Model):
    quantity_reserved = models.IntegerField()
    reserved_until = models.DateTimeField()
    checkout_line = models.ForeignKey(CheckoutCheckoutline, models.DO_NOTHING)
    stock = models.ForeignKey(WarehouseStock, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_reservation'
        unique_together = (('checkout_line', 'stock'),)





class WarehouseWarehouseShippingZones(models.Model):
    warehouse = models.ForeignKey(WarehouseWarehouse, models.DO_NOTHING)
    shippingzone = models.ForeignKey(ShippingShippingzone, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_warehouse_shipping_zones'
        unique_together = (('warehouse', 'shippingzone'),)


class WebhookWebhook(models.Model):
    target_url = models.CharField(max_length=255)
    is_active = models.BooleanField()
    secret_key = models.CharField(max_length=255, blank=True, null=True)
    app = models.ForeignKey(AppApp, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webhook_webhook'


class WebhookWebhookevent(models.Model):
    event_type = models.CharField(max_length=128)
    webhook = models.ForeignKey(WebhookWebhook, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'webhook_webhookevent'
