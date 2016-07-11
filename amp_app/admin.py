from django.contrib import admin
from models import *
# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name','government']

class Customer(admin.ModelAdmin):
    list_display = ['name','address','account_number','is_customer']

class Item(admin.ModelAdmin):
    list_display = ['name','price','price_refactor']

class InvoiceLineForm(admin.TabularInline):
    model = InvoiceLine
    fk_name='invoice'
    max_num=1

class invoice(admin.ModelAdmin):
    list_display = ['id','invoice_date','area','customer','car_number','car_owner','car_driver','invoiceItem']
    inlines = [InvoiceLineForm,]
    search_fields = ['invoice_date']

    def invoiceItem(self,obj):
        return InvoiceLine.objects.get(id=obj.id).item.name

admin.site.register(Areas,AreaAdmin)
admin.site.register(Items,Item)
admin.site.register(Customers,Customer)
admin.site.register(Invoice,invoice)
# admin.site.register(InvoiceLine)