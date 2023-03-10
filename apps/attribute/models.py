from django.db import models

from apps.page.models import PagePagetype, PagePage
from apps.product.models import ProductProduct, ProductProductvariant, ProductProducttype


# Create your models here.

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



class AttributeAttributevariant(models.Model):
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)
    product_type = models.ForeignKey(ProductProducttype, models.DO_NOTHING)
    sort_order = models.IntegerField(blank=True, null=True)
    variant_selection = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'attribute_attributevariant'
        unique_together = (('attribute', 'product_type'),)



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




class AttributeAttributeproduct(models.Model):
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)
    product_type = models.ForeignKey(ProductProducttype, models.DO_NOTHING)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_attributeproduct'
        unique_together = (('attribute', 'product_type'),)



class AttributeAttributepage(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)
    page_type = models.ForeignKey(PagePagetype, models.DO_NOTHING)


class AttributeAssignedpageattribute(models.Model):
    assignment = models.ForeignKey(AttributeAttributepage, models.DO_NOTHING)
    page = models.ForeignKey(PagePage, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'attribute_assignedpageattribute'




    class Meta:
        managed = False
        db_table = 'attribute_attributepage'
        unique_together = (('attribute', 'page_type'),)


class AttributeAssignedpageattributevalue(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    assignment = models.ForeignKey(AttributeAssignedpageattribute, models.DO_NOTHING)
    value = models.ForeignKey(AttributeAttributevalue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedpageattributevalue'
        unique_together = (('value', 'assignment'),)


class AttributeAssignedproductattribute(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    assignment = models.ForeignKey(AttributeAttributeproduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedproductattribute'
        unique_together = (('product', 'assignment'),)


class AttributeAssignedproductattributevalue(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    assignment = models.ForeignKey(AttributeAssignedproductattribute, models.DO_NOTHING)
    value = models.ForeignKey(AttributeAttributevalue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedproductattributevalue'
        unique_together = (('value', 'assignment'),)


class AttributeAssignedvariantattribute(models.Model):
    variant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)
    assignment = models.ForeignKey(AttributeAttributevariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedvariantattribute'
        unique_together = (('variant', 'assignment'),)


class AttributeAssignedvariantattributevalue(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    assignment = models.ForeignKey(AttributeAssignedvariantattribute, models.DO_NOTHING)
    value = models.ForeignKey(AttributeAttributevalue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_assignedvariantattributevalue'
        unique_together = (('value', 'assignment'),)





class AttributeAttributetranslation(models.Model):
    language_code = models.CharField(max_length=35)
    name = models.CharField(max_length=100)
    attribute = models.ForeignKey(AttributeAttribute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attribute_attributetranslation'
        unique_together = (('language_code', 'attribute'),)




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
    product_type = models.ForeignKey(ProductProducttype, models.DO_NOTHING)
    sort_order = models.IntegerField(blank=True, null=True)
    variant_selection = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'attribute_attributevariant'
        unique_together = (('attribute', 'product_type'),)