from rest_framework import viewsets

from .models import AccountAddress, AccountUser, AccountCustomernote, AccountStaffnotificationrecipient, AccountUserAddresses, AccountUserGroups, AccountUserUserPermissions
from .serializers import AccountAddressSerializer, AccountUserSerializer, AccountCustomernoteSerializer, AccountStaffnotificationrecipientSerializer, AccountUserAddressesSerializer, AccountUserGroupsSerializer, AccountUserUserPermissionsSerializer

class AccountAddressViewSet(viewsets.ModelViewSet):
    queryset = AccountAddress.objects.all()
    serializer_class = AccountAddressSerializer

class AccountUserViewSet(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer

class AccountCustomernoteViewSet(viewsets.ModelViewSet):
    queryset = AccountCustomernote.objects.all()
    serializer_class = AccountCustomernoteSerializer

class AccountStaffnotificationrecipientViewSet(viewsets.ModelViewSet):
    queryset = AccountStaffnotificationrecipient.objects.all()
    serializer_class = AccountStaffnotificationrecipientSerializer

class AccountUserAddressesViewSet(viewsets.ModelViewSet):
    queryset = AccountUserAddresses.objects.all()
    serializer_class = AccountUserAddressesSerializer

class AccountUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AccountUserGroups.objects.all()
    serializer_class = AccountUserGroupsSerializer

class AccountUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AccountUserUserPermissions.objects.all()
    serializer_class = AccountUserUserPermissionsSerializer