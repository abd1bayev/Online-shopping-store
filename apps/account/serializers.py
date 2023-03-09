from rest_framework import serializers
from .models import AccountAddress, AccountUser, AccountCustomernote, AccountStaffnotificationrecipient, \
    AccountUserAddresses, AccountUserGroups, AccountUserUserPermissions


class AccountAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountAddress
        fields = '__all__'


class AccountUserSerializer(serializers.ModelSerializer):
    default_billing_address = AccountAddressSerializer()
    default_shipping_address = AccountAddressSerializer()

    class Meta:
        model = AccountUser
        fields = '__all__'


class AccountCustomernoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCustomernote
        fields = '__all__'


class AccountStaffnotificationrecipientSerializer(serializers.ModelSerializer):
    user = AccountUserSerializer()

    class Meta:
        model = AccountStaffnotificationrecipient
        fields = '__all__'


class AccountUserAddressesSerializer(serializers.ModelSerializer):
    user = AccountUserSerializer()
    address = AccountAddressSerializer()

    class Meta:
        model = AccountUserAddresses
        fields = '__all__'


class AccountUserGroupsSerializer(serializers.ModelSerializer):
    user = AccountUserSerializer()
    group = serializers.StringRelatedField()

    class Meta:
        model = AccountUserGroups
        fields = '__all__'


class AccountUserUserPermissionsSerializer(serializers.ModelSerializer):
    user = AccountUserSerializer()
    permission = serializers.StringRelatedField()

    class Meta:
        model = AccountUserUserPermissions
        fields = '__all__'