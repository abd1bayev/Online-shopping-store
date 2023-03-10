from django.db import models

from apps.account.models import AccountUser
from apps.app.models import AppApp
from apps.order.models import OrderOrder
from apps.page.models import PagePage
from apps.product.models import ProductCategory, ProductCollection


# Create your models here.


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
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(ProductCollection, models.DO_NOTHING, blank=True, null=True)
    menu = models.ForeignKey(MenuMenu, models.DO_NOTHING)
    page = models.ForeignKey(PagePage, models.DO_NOTHING, blank=True, null=True)
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
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_invoice'


class InvoiceInvoiceevent(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=255)
    parameters = models.JSONField()
    invoice = models.ForeignKey(InvoiceInvoice, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_invoiceevent'