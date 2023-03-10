from django.db import models

from apps.checkout.models import ChannelChannel
from apps.order.models import OrderOrder
from apps.product.models import ProductCategory, \
    ProductCollection, ProductProduct, \
    ProductProductvariant


# Create your models here.


class DiscountInstallmentplan(models.Model):
    months = models.SmallIntegerField()
    percent = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'discount_installmentplan'


class DiscountOrderdiscount(models.Model):
    type = models.CharField(max_length=10)
    value_type = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=12, decimal_places=3)
    amount_value = models.DecimalField(max_digits=12, decimal_places=3)
    currency = models.CharField(max_length=3)
    name = models.CharField(max_length=255, blank=True, null=True)
    translated_name = models.CharField(max_length=255, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_orderdiscount'


class DiscountSale(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    end_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField()
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_sale'


class DiscountSaleCategories(models.Model):
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_sale_categories'
        unique_together = (('sale', 'category'),)


class DiscountSaleCollections(models.Model):
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)
    collection = models.ForeignKey(ProductCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_sale_collections'
        unique_together = (('sale', 'collection'),)


class DiscountSaleProducts(models.Model):
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_sale_products'
        unique_together = (('sale', 'product'),)


class DiscountSaleVariants(models.Model):
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)
    productvariant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_sale_variants'
        unique_together = (('sale', 'productvariant'),)


class DiscountSalechannellisting(models.Model):
    discount_value = models.DecimalField(max_digits=12, decimal_places=3)
    currency = models.CharField(max_length=3)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_salechannellisting'
        unique_together = (('sale', 'channel'),)


class DiscountSaletranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=255, blank=True, null=True)
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_saletranslation'
        unique_together = (('language_code', 'sale'),)


class DiscountVoucher(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=255)
    usage_limit = models.IntegerField(blank=True, null=True)
    used = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    discount_value_type = models.CharField(max_length=10)
    apply_once_per_order = models.BooleanField()
    countries = models.CharField(max_length=749)
    min_checkout_items_quantity = models.IntegerField(blank=True, null=True)
    apply_once_per_customer = models.BooleanField()
    only_for_staff = models.BooleanField()
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_voucher'


class DiscountVoucherCategories(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucher_categories'
        unique_together = (('voucher', 'category'),)


class DiscountVoucherCollections(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    collection = models.ForeignKey(ProductCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucher_collections'
        unique_together = (('voucher', 'collection'),)


class DiscountVoucherProducts(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucher_products'
        unique_together = (('voucher', 'product'),)


class DiscountVoucherVariants(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    productvariant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucher_variants'
        unique_together = (('voucher', 'productvariant'),)


class DiscountVoucherchannellisting(models.Model):
    discount_value = models.DecimalField(max_digits=12, decimal_places=3)
    currency = models.CharField(max_length=3)
    min_spent_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucherchannellisting'
        unique_together = (('voucher', 'channel'),)


class DiscountVouchercustomer(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    customer_email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'discount_vouchercustomer'
        unique_together = (('voucher', 'customer_email'),)


class DiscountVouchertranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=255, blank=True, null=True)
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_vouchertranslation'
        unique_together = (('language_code', 'voucher'),)