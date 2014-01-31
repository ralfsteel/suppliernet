from django.contrib import admin
from producers.models import Client, Pricelist, Promotional
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('number','name','address','zipcode','city','phone','phones','fax','email')


class PricelistAdmin(admin.ModelAdmin):
    list_display = ('item_name','item_price')


class PromotionalAdmin(admin.ModelAdmin):
    list_display = ('item_title','detail')



admin.site.register(Client, ClientAdmin)
admin.site.register(Promotional, PromotionalAdmin)
admin.site.register(Pricelist, PricelistAdmin)


