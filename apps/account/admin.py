from django.contrib import admin
from .models import AccountAddress, AccountUser, AccountCustomernote, AccountStaffnotificationrecipient, AccountUserAddresses, AccountUserGroups, AccountUserUserPermissions


class AccountAddressAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'country')


class AccountUserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('-date_joined',)



class AccountCustomernoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'content', 'is_public')
    list_filter = ('is_public',)


class AccountStaffnotificationrecipientAdmin(admin.ModelAdmin):
    list_display = ('user', 'staff_email', 'active')


class AccountUserAddressesAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')


class AccountUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')


class AccountUserUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission')


admin.site.register(AccountAddress, AccountAddressAdmin)
admin.site.register(AccountUser, AccountUserAdmin)
admin.site.register(AccountCustomernote, AccountCustomernoteAdmin)
admin.site.register(AccountStaffnotificationrecipient, AccountStaffnotificationrecipientAdmin)
admin.site.register(AccountUserAddresses, AccountUserAddressesAdmin)
admin.site.register(AccountUserGroups, AccountUserGroupsAdmin)
admin.site.register(AccountUserUserPermissions, AccountUserUserPermissionsAdmin)