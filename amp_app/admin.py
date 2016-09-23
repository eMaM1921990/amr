from django import forms
from django.contrib import admin
from models import *
# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'government']


class Customer(admin.ModelAdmin):
    list_display = ['name', 'address', 'account_number', 'is_customer']


class Item(admin.ModelAdmin):
    list_display = ['name', 'price', 'price_refactor']


class InvoiceLineForm(admin.TabularInline):
    model = InvoiceLine
    fk_name = 'invoice'
    max_num = 1


class InvoiceForm(forms.ModelForm):
    area = forms.ModelChoiceField(queryset=Areas.objects.all().order_by('name'),
                                  widget=forms.Select(attrs={"onChange": 'get_customer()'}))
    customer = forms.ModelChoiceField(queryset=Customers.objects.filter(is_customer=True).order_by('name'),
                                      widget=forms.Select())
    car_owner = forms.ModelChoiceField(queryset=Customers.objects.filter(is_customer=False).order_by('name'),
                                       widget=forms.Select())

    customer_number = forms.CharField(max_length=30, label='Customer No.',widget=forms.TextInput(attrs={"onkeyup": 'get_customer_info()'}))

    class Meta:
        model = Invoice
        fields = ['invoice_date', 'customer_number', 'area', 'customer', 'car_number', 'car_owner', 'car_driver', 'invoice_number',
                  'delivery_distnation']

    class Media:
        js = ('//code.jquery.com/jquery-1.11.0.min.js', 'js/custom.js')


class invoice(admin.ModelAdmin):
    form = InvoiceForm
    list_display = ['id', 'invoice_number', 'invoice_date', 'area', 'customer', 'car_number', 'car_owner', 'car_driver',
                    'delivery_distnation', 'invoiceItem']
    inlines = [InvoiceLineForm, ]
    search_fields = ['invoice_date', 'area', 'customer', 'car_number', 'car_owner', 'car_driver', 'delivery_distnation',
                     'invoiceItem']
    list_filter = [ 'invoice_number', 'invoice_date', 'area', 'customer', 'car_number', 'car_owner', 'car_driver',
                    'delivery_distnation']
    def invoiceItem(self, obj):
        return InvoiceLine.objects.get(id=obj.id).item.name


admin.site.register(Areas, AreaAdmin)
admin.site.register(Items, Item)
admin.site.register(Customers, Customer)
admin.site.register(Invoice, invoice)
# admin.site.register(InvoiceLine)