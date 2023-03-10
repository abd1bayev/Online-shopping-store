from django.db import models


class AccountAddress(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    company_name = models.CharField(max_length=256)
    street_address_1 = models.CharField(max_length=256)
    street_address_2 = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    country_area = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    city_area = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'account_address'


# class AccountCustomerevent(models.Model):
#     date = models.DateTimeField()
#     type = models.CharField(max_length=255)
#     parameters = models.JSONField()
#     order = models.ForeignKey('OrderOrder', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey('AccountUser', models.DO_NOTHING, blank=True, null=True)
#     app = models.ForeignKey('AppApp', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'account_customerevent'



class AccountStaffnotificationrecipient(models.Model):
    active = models.BooleanField()
    user = models.OneToOneField('AccountUser', models.DO_NOTHING, blank=True, null=True)
    staff_email = models.CharField(unique=True, max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_staffnotificationrecipient'


class AccountUser(models.Model):
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    default_billing_address = models.ForeignKey(AccountAddress, models.DO_NOTHING, blank=True, null=True)
    default_shipping_address = models.ForeignKey(AccountAddress, models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    jwt_token_key = models.CharField(max_length=12)
    language_code = models.CharField(max_length=35)
    search_document = models.TextField()
    phone = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'account_user'



class AccountCustomernote(models.Model):
    date = models.DateTimeField()
    content = models.TextField()
    is_public = models.BooleanField()
    customer = models.ForeignKey(AccountUser, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_customernote'


class AccountUserAddresses(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    address = models.ForeignKey(AccountAddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_addresses'
        unique_together = (('user', 'address'),)


class AccountUserGroups(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_groups'
        unique_together = (('user', 'group'),)


class AccountUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_user_permissions'
        unique_together = (('user', 'permission'),)















class AppApp(models.Model):
    private_metadata = models.JSONField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=60)
    created = models.DateTimeField()
    is_active = models.BooleanField()
    about_app = models.TextField(blank=True, null=True)
    app_url = models.CharField(max_length=200, blank=True, null=True)
    configuration_url = models.CharField(max_length=200, blank=True, null=True)
    data_privacy = models.TextField(blank=True, null=True)
    data_privacy_url = models.CharField(max_length=200, blank=True, null=True)
    homepage_url = models.CharField(max_length=200, blank=True, null=True)
    identifier = models.CharField(max_length=256, blank=True, null=True)
    support_url = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=60)
    version = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_app'


class AppAppPermissions(models.Model):
    app = models.ForeignKey(AppApp, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_app_permissions'
        unique_together = (('app', 'permission'),)


class AppAppextension(models.Model):
    label = models.CharField(max_length=256)
    url = models.CharField(max_length=200)
    app = models.ForeignKey(AppApp, models.DO_NOTHING)
    mount = models.CharField(max_length=256)
    target = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'app_appextension'


class AppAppextensionPermissions(models.Model):
    appextension = models.ForeignKey(AppAppextension, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_appextension_permissions'
        unique_together = (('appextension', 'permission'),)


class AppAppinstallation(models.Model):
    status = models.CharField(max_length=50)
    message = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    app_name = models.CharField(max_length=60)
    manifest_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'app_appinstallation'


class AppAppinstallationPermissions(models.Model):
    appinstallation = models.ForeignKey(AppAppinstallation, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_appinstallation_permissions'
        unique_together = (('appinstallation', 'permission'),)


class AppApptoken(models.Model):
    name = models.CharField(max_length=128)
    auth_token = models.CharField(unique=True, max_length=30)
    app = models.ForeignKey(AppApp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_apptoken'






class AttributeAssignedpageattribute(models.Model):
    assignment = models.ForeignKey('AttributeAttributepage', models.DO_NOTHING)
    page = models.ForeignKey('PagePage', models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'attribute_assignedpageattribute'


class AttributeAssignedpageattributevalue(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    assignment = models.ForeignKey(AttributeAssignedpageattribute, models.DO_NOTHING)
    value = models.ForeignKey('AttributeAttributevalue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedpageattributevalue'
        unique_together = (('value', 'assignment'),)


class AttributeAssignedproductattribute(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    assignment = models.ForeignKey('AttributeAttributeproduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedproductattribute'
        unique_together = (('product', 'assignment'),)


class AttributeAssignedproductattributevalue(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    assignment = models.ForeignKey(AttributeAssignedproductattribute, models.DO_NOTHING)
    value = models.ForeignKey('AttributeAttributevalue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedproductattributevalue'
        unique_together = (('value', 'assignment'),)


class AttributeAssignedvariantattribute(models.Model):
    variant = models.ForeignKey('ProductProductvariant', models.DO_NOTHING)
    assignment = models.ForeignKey('AttributeAttributevariant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedvariantattribute'
        unique_together = (('variant', 'assignment'),)


class AttributeAssignedvariantattributevalue(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    assignment = models.ForeignKey(AttributeAssignedvariantattribute, models.DO_NOTHING)
    value = models.ForeignKey('AttributeAttributevalue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedvariantattributevalue'
        unique_together = (('value', 'assignment'),)


class AttributeAttribute(models.Model):
    slug = models.CharField(unique=True, max_length=250)
    name = models.CharField(max_length=255)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    input_type = models.CharField(max_length=50)
    available_in_grid = models.BooleanField()
    visible_in_storefront = models.BooleanField()
    filterable_in_dashboard = models.BooleanField()
    filterable_in_storefront = models.BooleanField()
    value_required = models.BooleanField()
    storefront_search_position = models.IntegerField()
    is_variant_only = models.BooleanField()
    type = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_attribute'


class AttributeAttributepage(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)
    page_type = models.ForeignKey('PagePagetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_attributepage'
        unique_together = (('attribute', 'page_type'),)


class AttributeAttributeproduct(models.Model):
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)
    product_type = models.ForeignKey('ProductProducttype', models.DO_NOTHING)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_attributeproduct'
        unique_together = (('attribute', 'product_type'),)


class AttributeAttributetranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=100)
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_attributetranslation'
        unique_together = (('language_code', 'attribute'),)


class AttributeAttributevalue(models.Model):
    name = models.CharField(max_length=250)
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)
    slug = models.CharField(max_length=255)
    sort_order = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=9)
    content_type = models.CharField(max_length=50, blank=True, null=True)
    file_url = models.CharField(max_length=200, blank=True, null=True)
    rich_text = models.JSONField(blank=True, null=True)
    boolean = models.BooleanField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_attributevalue'
        unique_together = (('slug', 'attribute'),)


class AttributeAttributevaluetranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=100)
    attribute_value = models.ForeignKey(AttributeAttributevalue, models.DO_NOTHING)
    rich_text = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_attributevaluetranslation'
        unique_together = (('language_code', 'attribute_value'),)


class AttributeAttributevariant(models.Model):
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)
    product_type = models.ForeignKey('ProductProducttype', models.DO_NOTHING)
    sort_order = models.IntegerField(blank=True, null=True)
    variant_selection = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'attribute_attributevariant'
        unique_together = (('attribute', 'product_type'),)






class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)




class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class ChannelChannel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=255)
    is_active = models.BooleanField()
    currency_code = models.CharField(max_length=3)
    default_country = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'channel_channel'





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
    shipping_method = models.ForeignKey('ShippingShippingmethod', models.DO_NOTHING, blank=True, null=True)
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
    collection_point = models.ForeignKey('WarehouseWarehouse', models.DO_NOTHING, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkout_checkout'


class CheckoutCheckoutGiftCards(models.Model):
    checkout = models.ForeignKey(CheckoutCheckout, models.DO_NOTHING)
    giftcard = models.ForeignKey('GiftcardGiftcard', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'checkout_checkout_gift_cards'
        unique_together = (('checkout', 'giftcard'),)


class CheckoutCheckoutline(models.Model):
    quantity = models.IntegerField()
    checkout = models.ForeignKey(CheckoutCheckout, models.DO_NOTHING)
    variant = models.ForeignKey('ProductProductvariant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'checkout_checkoutline'






class CoreEventdelivery(models.Model):
    created_at = models.DateTimeField()
    status = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    payload = models.ForeignKey('CoreEventpayload', models.DO_NOTHING, blank=True, null=True)
    webhook = models.ForeignKey('WebhookWebhook', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_eventdelivery'


class CoreEventdeliveryattempt(models.Model):
    created_at = models.DateTimeField()
    task_id = models.CharField(max_length=255, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_headers = models.TextField(blank=True, null=True)
    request_headers = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255)
    delivery = models.ForeignKey(CoreEventdelivery, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_eventdeliveryattempt'




class CoreEventpayload(models.Model):
    payload = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_eventpayload'


class CsvExportevent(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=255)
    parameters = models.JSONField()
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)
    export_file = models.ForeignKey('CsvExportfile', models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csv_exportevent'


class CsvExportfile(models.Model):
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    content_file = models.CharField(max_length=100, blank=True, null=True)
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csv_exportfile'


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
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING, blank=True, null=True)

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
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_sale_categories'
        unique_together = (('sale', 'category'),)


class DiscountSaleCollections(models.Model):
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)
    collection = models.ForeignKey('ProductCollection', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_sale_collections'
        unique_together = (('sale', 'collection'),)


class DiscountSaleProducts(models.Model):
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_sale_products'
        unique_together = (('sale', 'product'),)


class DiscountSaleVariants(models.Model):
    sale = models.ForeignKey(DiscountSale, models.DO_NOTHING)
    productvariant = models.ForeignKey('ProductProductvariant', models.DO_NOTHING)

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
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucher_categories'
        unique_together = (('voucher', 'category'),)


class DiscountVoucherCollections(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    collection = models.ForeignKey('ProductCollection', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucher_collections'
        unique_together = (('voucher', 'collection'),)


class DiscountVoucherProducts(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discount_voucher_products'
        unique_together = (('voucher', 'product'),)


class DiscountVoucherVariants(models.Model):
    voucher = models.ForeignKey(DiscountVoucher, models.DO_NOTHING)
    productvariant = models.ForeignKey('ProductProductvariant', models.DO_NOTHING)

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




class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)
    expire_seconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoPricesOpenexchangeratesConversionrate(models.Model):
    to_currency = models.CharField(unique=True, max_length=3)
    rate = models.DecimalField(max_digits=20, decimal_places=12)
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_prices_openexchangerates_conversionrate'


class DjangoPricesVatlayerRatetypes(models.Model):
    types = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_prices_vatlayer_ratetypes'


class DjangoPricesVatlayerVat(models.Model):
    country_code = models.CharField(max_length=2)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_prices_vatlayer_vat'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class GiftcardGiftcard(models.Model):
    code = models.CharField(unique=True, max_length=16)
    created = models.DateTimeField()
    last_used_on = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    initial_balance_amount = models.DecimalField(max_digits=12, decimal_places=3)
    current_balance_amount = models.DecimalField(max_digits=12, decimal_places=3)
    currency = models.CharField(max_length=3)
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    used_by = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    fulfillment_line = models.ForeignKey('OrderFulfillmentline', models.DO_NOTHING, blank=True, null=True)
    created_by_phone = models.CharField(max_length=128, blank=True, null=True)
    used_by_phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'giftcard_giftcard'


class GiftcardGiftcardTags(models.Model):
    giftcard = models.ForeignKey(GiftcardGiftcard, models.DO_NOTHING)
    giftcardtag = models.ForeignKey('GiftcardGiftcardtag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'giftcard_giftcard_tags'
        unique_together = (('giftcard', 'giftcardtag'),)


class GiftcardGiftcardevent(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=255)
    parameters = models.JSONField()
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)
    gift_card = models.ForeignKey(GiftcardGiftcard, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'giftcard_giftcardevent'


class GiftcardGiftcardtag(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'giftcard_giftcardtag'


class HomepageBanner(models.Model):
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.CharField(max_length=100, blank=True, null=True)
    background_image_alt = models.CharField(max_length=128)
    redirect_url = models.CharField(max_length=200)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    type = models.CharField(max_length=10)
    view_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'homepage_banner'


class HomepageBannertranslation(models.Model):
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    language_code = models.CharField(max_length=10)
    background_image = models.CharField(max_length=100, blank=True, null=True)
    background_image_alt = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()
    banner = models.ForeignKey(HomepageBanner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'homepage_bannertranslation'
        unique_together = (('language_code', 'banner'),)


class InvoiceInvoice(models.Model):
    private_metadata = models.JSONField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    number = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    external_url = models.CharField(max_length=2048, blank=True, null=True)
    invoice_file = models.CharField(max_length=100)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_invoice'


class InvoiceInvoiceevent(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=255)
    parameters = models.JSONField()
    invoice = models.ForeignKey(InvoiceInvoice, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_invoiceevent'


class MenuMenu(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=255)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_menu'


class MenuMenuitem(models.Model):
    name = models.CharField(max_length=128)
    sort_order = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey('ProductCollection', models.DO_NOTHING, blank=True, null=True)
    menu = models.ForeignKey(MenuMenu, models.DO_NOTHING)
    page = models.ForeignKey('PagePage', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_menuitem'


class MenuMenuitemtranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=128)
    menu_item = models.ForeignKey(MenuMenuitem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_menuitemtranslation'
        unique_together = (('language_code', 'menu_item'),)








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
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING)
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
    order_line = models.ForeignKey('OrderOrderline', models.DO_NOTHING)
    quantity = models.IntegerField()
    fulfillment = models.ForeignKey(OrderFulfillment, models.DO_NOTHING)
    stock = models.ForeignKey('WarehouseStock', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_fulfillmentline'


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
    shipping_method = models.ForeignKey('ShippingShippingmethod', models.DO_NOTHING, blank=True, null=True)
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
    collection_point = models.ForeignKey('WarehouseWarehouse', models.DO_NOTHING, blank=True, null=True)
    collection_point_name = models.CharField(max_length=255, blank=True, null=True)
    search_document = models.TextField()
    user_phone = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'order_order'


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


class OrderOrderline(models.Model):
    product_name = models.CharField(max_length=386)
    product_sku = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price_net_amount = models.DecimalField(max_digits=12, decimal_places=3)
    unit_price_gross_amount = models.DecimalField(max_digits=12, decimal_places=3)
    is_shipping_required = models.BooleanField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    quantity_fulfilled = models.IntegerField()
    variant = models.ForeignKey('ProductProductvariant', models.DO_NOTHING, blank=True, null=True)
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


class PagePage(models.Model):
    slug = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=250)
    content = models.JSONField(blank=True, null=True)
    created = models.DateTimeField()
    is_published = models.BooleanField()
    publication_date = models.DateField(blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    page_type = models.ForeignKey('PagePagetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'page_page'


class PagePagetranslation(models.Model):
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    language_code = models.CharField(max_length=35)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.JSONField(blank=True, null=True)
    page = models.ForeignKey(PagePage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'page_pagetranslation'
        unique_together = (('language_code', 'page'),)


class PagePagetype(models.Model):
    private_metadata = models.JSONField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'page_pagetype'


class PaymartBuyer(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(unique=True, max_length=128)
    buyer_id = models.CharField(max_length=50)
    user_status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'paymart_buyer'


class PaymartContract(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_id = models.BigIntegerField(unique=True, blank=True, null=True)
    products = models.TextField()  # This field type is a guess.
    limit = models.SmallIntegerField()
    payment_date = models.SmallIntegerField(blank=True, null=True)
    buyer_phone = models.CharField(max_length=13)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    product_variant = models.ForeignKey('ProductProductvariant', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=12)
    address = models.CharField(max_length=155)
    total_count = models.IntegerField()
    total_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'paymart_contract'


class PaymentCurrency(models.Model):
    currency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_currency'


class PaymentPayment(models.Model):
    gateway = models.CharField(max_length=255)
    is_active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    charge_status = models.CharField(max_length=20)
    billing_first_name = models.CharField(max_length=256)
    billing_last_name = models.CharField(max_length=256)
    billing_company_name = models.CharField(max_length=256)
    billing_address_1 = models.CharField(max_length=256)
    billing_address_2 = models.CharField(max_length=256)
    billing_city = models.CharField(max_length=256)
    billing_city_area = models.CharField(max_length=128)
    billing_postal_code = models.CharField(max_length=256)
    billing_country_code = models.CharField(max_length=2)
    billing_country_area = models.CharField(max_length=256)
    customer_ip_address = models.GenericIPAddressField(blank=True, null=True)
    cc_brand = models.CharField(max_length=40)
    cc_exp_month = models.IntegerField(blank=True, null=True)
    cc_exp_year = models.IntegerField(blank=True, null=True)
    cc_first_digits = models.CharField(max_length=6)
    cc_last_digits = models.CharField(max_length=4)
    extra_data = models.TextField()
    token = models.CharField(max_length=512)
    currency = models.CharField(max_length=3)
    total = models.DecimalField(max_digits=12, decimal_places=3)
    captured_amount = models.DecimalField(max_digits=12, decimal_places=3)
    checkout = models.ForeignKey(CheckoutCheckout, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING, blank=True, null=True)
    to_confirm = models.BooleanField()
    payment_method_type = models.CharField(max_length=256)
    return_url = models.CharField(max_length=200, blank=True, null=True)
    psp_reference = models.CharField(max_length=512, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    store_payment_method = models.CharField(max_length=11)
    partial = models.BooleanField()
    billing_phone = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'payment_payment'


class PaymentTransaction(models.Model):
    created = models.DateTimeField()
    token = models.CharField(max_length=512)
    kind = models.CharField(max_length=25)
    is_success = models.BooleanField()
    error = models.CharField(max_length=256, blank=True, null=True)
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    payment = models.ForeignKey(PaymentPayment, models.DO_NOTHING)
    customer_id = models.CharField(max_length=256, blank=True, null=True)
    action_required = models.BooleanField()
    action_required_data = models.JSONField()
    already_processed = models.BooleanField()
    canceled = models.DateTimeField(blank=True, null=True)
    performed = models.DateTimeField(blank=True, null=True)
    request_id = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=55)
    reason = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PluginsEmailtemplate(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    plugin_configuration = models.ForeignKey('PluginsPluginconfiguration', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'plugins_emailtemplate'


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


class ProductCollectionproduct(models.Model):
    collection = models.ForeignKey(ProductCollection, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_collectionproduct'
        unique_together = (('collection', 'product'),)


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


class ProductDigitalcontent(models.Model):
    use_default_settings = models.BooleanField()
    automatic_fulfillment = models.BooleanField()
    content_type = models.CharField(max_length=128)
    content_file = models.CharField(max_length=100)
    max_downloads = models.IntegerField(blank=True, null=True)
    url_valid_days = models.IntegerField(blank=True, null=True)
    product_variant = models.OneToOneField('ProductProductvariant', models.DO_NOTHING)
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
    line = models.OneToOneField(OrderOrderline, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_digitalcontenturl'


class ProductProduct(models.Model):
    name = models.CharField(max_length=250)
    description = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    product_type = models.ForeignKey('ProductProducttype', models.DO_NOTHING)
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


class ShippingShippingmethod(models.Model):
    name = models.CharField(max_length=100)
    maximum_order_weight = models.FloatField(blank=True, null=True)
    minimum_order_weight = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=30)
    shipping_zone = models.ForeignKey('ShippingShippingzone', models.DO_NOTHING)
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


class ShippingShippingzoneChannels(models.Model):
    shippingzone = models.ForeignKey(ShippingShippingzone, models.DO_NOTHING)
    channel = models.ForeignKey(ChannelChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_shippingzone_channels'
        unique_together = (('shippingzone', 'channel'),)


class SiteSitesettings(models.Model):
    header_text = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    site = models.OneToOneField(DjangoSite, models.DO_NOTHING)
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


class WarehouseAllocation(models.Model):
    quantity_allocated = models.IntegerField()
    order_line = models.ForeignKey(OrderOrderline, models.DO_NOTHING)
    stock = models.ForeignKey('WarehouseStock', models.DO_NOTHING)

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
    stock = models.ForeignKey('WarehouseStock', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_reservation'
        unique_together = (('checkout_line', 'stock'),)


class WarehouseStock(models.Model):
    quantity = models.IntegerField()
    product_variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)
    warehouse = models.ForeignKey('WarehouseWarehouse', models.DO_NOTHING)
    quantity_allocated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'warehouse_stock'
        unique_together = (('warehouse', 'product_variant'),)


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


class WishlistWishlist(models.Model):
    created_at = models.DateTimeField()
    token = models.UUIDField(unique=True)
    user = models.OneToOneField(AccountUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlist'


class WishlistWishlistitem(models.Model):
    created_at = models.DateTimeField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    wishlist = models.ForeignKey(WishlistWishlist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlistitem'
        unique_together = (('wishlist', 'product'),)


class WishlistWishlistitemVariants(models.Model):
    wishlistitem = models.ForeignKey(WishlistWishlistitem, models.DO_NOTHING)
    productvariant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlistitem_variants'
        unique_together = (('wishlistitem', 'productvariant'),)
