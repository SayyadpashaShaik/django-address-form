from django.contrib import admin

from address.models import Address

# Register your models here.

@admin.register(Address)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','pincode','state','address','locality','city','type_of_address']

# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('name','contact','pincode','state','address','locality','city','addressType')
# admin.site.register(Address, AddressAdmin)
