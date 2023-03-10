from django.db import models

from apps.account.models import AccountUser
from apps.app.models import AppApp
from apps.sitesettings.models import WebhookWebhook


# Create your models here.



class CoreEventpayload(models.Model):
    payload = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_eventpayload'





class CoreEventdelivery(models.Model):
    created_at = models.DateTimeField()
    status = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    payload = models.ForeignKey(CoreEventpayload, models.DO_NOTHING, blank=True, null=True)
    webhook = models.ForeignKey(WebhookWebhook, models.DO_NOTHING, blank=True, null=True)

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




class CsvExportevent(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=255)
    parameters = models.JSONField()
    app = models.ForeignKey(AppApp, models.DO_NOTHING, blank=True, null=True)
    export_file = models.ForeignKey(CsvExportfile, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csv_exportevent'

