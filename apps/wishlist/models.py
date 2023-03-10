from django.db import models

from apps.account.models import AccountUser
from apps.product.models import ProductProduct, ProductProductvariant


# Create your models here.


class WishlistWishlist(models.Model):
    created_at = models.DateTimeField()
    token = models.UUIDField(unique=True)
    user = models.OneToOneField(AccountUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlist'


class WishlistWishlistitem(models.Model):
    created_at = models.DateTimeField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    wishlist = models.ForeignKey(WishlistWishlist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlistitem'
        unique_together = (('wishlist', 'product'),)


class WishlistWishlistitemVariants(models.Model):
    wishlistitem = models.ForeignKey(WishlistWishlistitem, models.DO_NOTHING)
    productvariant = models.ForeignKey(ProductProductvariant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlistitem_variants'
        unique_together = (('wishlistitem', 'productvariant'),)