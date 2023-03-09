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



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)



class AccountUser(models.Model):
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    default_billing_address = models.ForeignKey(
        AccountAddress,
        related_name='billing_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    default_shipping_address = models.ForeignKey(
        AccountAddress,
        related_name='shipping_users',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
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



class AccountCustomernote(models.Model):
    date = models.DateTimeField()
    content = models.TextField()
    is_public = models.BooleanField()
    user = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)



class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)



class AccountStaffnotificationrecipient(models.Model):
    active = models.BooleanField()
    user = models.OneToOneField(AccountUser, models.DO_NOTHING, blank=True, null=True)
    staff_email = models.CharField(unique=True, max_length=254, blank=True, null=True)



class AccountUserAddresses(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    address = models.ForeignKey(AccountAddress, models.DO_NOTHING)



class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    codename = models.CharField(max_length=100)



class AccountUserGroups(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)


class AccountUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

