from django.urls import path, include
from rest_framework import routers
from .views import AccountAddressViewSet, \
    AccountUserViewSet, AccountCustomernoteViewSet,\
    AccountStaffnotificationrecipientViewSet, \
    AccountUserAddressesViewSet, AccountUserGroupsViewSet, \
    AccountUserUserPermissionsViewSet



router = routers.DefaultRouter()
router.register(r'account-addresses', AccountAddressViewSet)
router.register(r'account-users', AccountUserViewSet)
router.register(r'account-customernotes', AccountCustomernoteViewSet)
router.register(r'account-staffnotificationrecipients', AccountStaffnotificationrecipientViewSet)
router.register(r'account-user-addresses', AccountUserAddressesViewSet)
router.register(r'account-user-groups', AccountUserGroupsViewSet)
router.register(r'account-user-user-permissions', AccountUserUserPermissionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]