from django.db import models


class AccountAddress(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    company_name = models.CharField(max_length=256)
    street_address_1 = models.CharField(max_length=256)
    street_address_2 = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    country_area = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128)
    city_area = models.CharField(max_length=128, blank=True, null=True)


class AccountUser(models.Model):
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
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
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, blank=True, null=True)


class AccountStaffnotificationrecipient(models.Model):
    active = models.BooleanField(default=True)
    user = models.OneToOneField(AccountUser, on_delete=models.CASCADE, blank=True, null=True)
    staff_email = models.CharField(unique=True, max_length=254, blank=True, null=True)


class AccountUserAddresses(models.Model):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    address = models.ForeignKey(AccountAddress, on_delete=models.CASCADE)


class AccountUserGroups(models.Model):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    group = models.ForeignKey('auth.Group', on_delete=models.CASCADE)


class AccountUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    permission = models.ForeignKey('auth.Permission', on_delete=models.CASCADE)
