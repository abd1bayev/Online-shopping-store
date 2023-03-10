from django.db import models

from apps.checkout.models import CheckoutCheckout
from apps.order.models import OrderOrder


# Create your models here.



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