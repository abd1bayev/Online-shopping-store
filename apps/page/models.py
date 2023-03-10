from django.db import models

# Create your models here.


class PagePagetype(models.Model):
    private_metadata = models.JSONField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'page_pagetype'


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
    page_type = models.ForeignKey(PagePagetype, models.DO_NOTHING)

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