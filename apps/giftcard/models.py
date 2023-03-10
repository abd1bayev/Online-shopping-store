from django.db import models

from apps.account.models import AccountUser
from apps.app.models import AppApp
from apps.order.models import OrderFulfillmentline
from apps.product.models import ProductProduct


# Create your models here.


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
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    used_by = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    fulfillment_line = models.ForeignKey(OrderFulfillmentline, models.DO_NOTHING, blank=True, null=True)
    created_by_phone = models.CharField(max_length=128, blank=True, null=True)
    used_by_phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'giftcard_giftcard'

class GiftcardGiftcardtag(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'giftcard_giftcardtag'


class GiftcardGiftcardTags(models.Model):
    giftcard = models.ForeignKey(GiftcardGiftcard, models.DO_NOTHING)
    giftcardtag = models.ForeignKey(GiftcardGiftcardtag, models.DO_NOTHING)

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

