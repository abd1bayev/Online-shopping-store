from django.db import models
from django.contrib.auth.models import Permission


# Create your models here.


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
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

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
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

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
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

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
