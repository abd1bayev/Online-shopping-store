# Generated by Django 4.1.7 on 2023-03-09 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('company_name', models.CharField(max_length=256)),
                ('street_address_1', models.CharField(max_length=256)),
                ('street_address_2', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=2)),
                ('country_area', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('city_area', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('password', models.CharField(max_length=128)),
                ('date_joined', models.DateTimeField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('avatar', models.CharField(blank=True, max_length=100, null=True)),
                ('private_metadata', models.JSONField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('jwt_token_key', models.CharField(max_length=12)),
                ('language_code', models.CharField(max_length=35)),
                ('search_document', models.TextField()),
                ('phone', models.CharField(max_length=128, unique=True)),
                ('default_billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_users', to='account.accountaddress')),
                ('default_shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_users', to='account.accountaddress')),
            ],
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.djangocontenttype')),
            ],
        ),
        migrations.CreateModel(
            name='AccountUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.authpermission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.accountuser')),
            ],
        ),
        migrations.CreateModel(
            name='AccountUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.authgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.accountuser')),
            ],
        ),
        migrations.CreateModel(
            name='AccountUserAddresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.accountaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.accountuser')),
            ],
        ),
        migrations.CreateModel(
            name='AccountStaffnotificationrecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('staff_email', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.accountuser')),
            ],
        ),
        migrations.CreateModel(
            name='AccountCustomernote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('is_public', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.accountuser')),
            ],
        ),
    ]