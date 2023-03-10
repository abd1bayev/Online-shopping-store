from django.db import models

from apps.checkout.models import ChannelChannel


# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=255)
    description = models.JSONField(blank=True, null=True)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    background_image = models.CharField(max_length=100, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    background_image_alt = models.CharField(max_length=128)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    description_plaintext = models.TextField()

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductProducttype(models.Model):
    name = models.CharField(max_length=250)
    has_variants = models.BooleanField()
    is_shipping_required = models.BooleanField()
    weight = models.FloatField()
    is_digital = models.BooleanField()
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    kind = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'product_producttype'


class ProductCategorytranslation(models.Model):
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_categorytranslation'
        unique_together = (('language_code', 'category'),)


class ProductCollection(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=255)
    background_image = models.CharField(max_length=100, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    background_image_alt = models.CharField(max_length=128)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_collection'


class ProductCollectionchannellisting(models.Model):
    publication_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField()
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    collection = models.ForeignKey(ProductCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_collectionchannellisting'
        unique_together = (('collection', 'channel'),)




class ProductCollectiontranslation(models.Model):
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=128, blank=True, null=True)
    collection = models.ForeignKey(ProductCollection, models.DO_NOTHING)
    description = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_collectiontranslation'
        unique_together = (('language_code', 'collection'),)


class ProductProduct(models.Model):
    name = models.CharField(max_length=250)
    description = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    product_type = models.ForeignKey(ProductProducttype, models.DO_NOTHING)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    charge_taxes = models.BooleanField()
    weight = models.FloatField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    default_variant = models.OneToOneField('ProductProductvariant', models.DO_NOTHING, blank=True, null=True)
    description_plaintext = models.TextField()
    rating = models.FloatField(blank=True, null=True)
    search_document = models.TextField()
    characteristics = models.JSONField(blank=True, null=True)
    in_discount = models.BooleanField()
    is_recommended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'product_product'

class ProductProductvariant(models.Model):
    sku = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    track_inventory = models.BooleanField()
    weight = models.FloatField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    is_preorder = models.BooleanField()
    preorder_end_date = models.DateTimeField(blank=True, null=True)
    preorder_global_threshold = models.IntegerField(blank=True, null=True)
    quantity_limit_per_customer = models.IntegerField(blank=True, null=True)
    in_discount = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'product_productvariant'


class ProductDigitalcontent(models.Model):
    use_default_settings = models.BooleanField()
    automatic_fulfillment = models.BooleanField()
    content_type = models.CharField(max_length=128)
    content_file = models.CharField(max_length=100)
    max_downloads = models.IntegerField(blank=True, null=True)
    url_valid_days = models.IntegerField(blank=True, null=True)
    product_variant = models.OneToOneField(ProductProductvariant, models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_digitalcontent'


class ProductDigitalcontenturl(models.Model):
    token = models.UUIDField(unique=True)
    created = models.DateTimeField()
    download_num = models.IntegerField()
    content = models.ForeignKey(ProductDigitalcontent, models.DO_NOTHING)
    # line = models.OneToOneField(OrderOrderline, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_digitalcontenturl'




class ProductProductchannellisting(models.Model):
    publication_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField()
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    discounted_price_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    currency = models.CharField(max_length=3)
    visible_in_listings = models.BooleanField()
    available_for_purchase = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_productchannellisting'
        unique_together = (('product', 'channel'),)




class ProductCollectionproduct(models.Model):
    collection = models.ForeignKey(ProductCollection, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_collectionproduct'
        unique_together = (('collection', 'product'),)



class ProductProductmedia(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    ppoi = models.CharField(max_length=20)
    alt = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    external_url = models.CharField(max_length=256, blank=True, null=True)
    oembed_data = models.JSONField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_productmedia'


class ProductProducttranslation(models.Model):
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_producttranslation'
        unique_together = (('language_code', 'product'),)







class ProductProductvariantchannellisting(models.Model):
    currency = models.CharField(max_length=3)
    price_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)
    variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)
    cost_price_amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    preorder_quantity_threshold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_productvariantchannellisting'
        unique_together = (('variant', 'channel'),)


class ProductProductvarianttranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=255)
    product_variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_productvarianttranslation'
        unique_together = (('language_code', 'product_variant'),)


class ProductVariantmedia(models.Model):
    media = models.ForeignKey(ProductProductmedia, models.DO_NOTHING)
    variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_variantmedia'
        unique_together = (('variant', 'media'),)




