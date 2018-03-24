from django.contrib import admin
from .models import Cliente, Order, OrderItem, FormaPagamento, PrazoPagamento


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'formapagamento', 'prazopagamento']
    list_filter = ['cliente', 'formapagamento', 'prazopagamento', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

admin.site.register(FormaPagamento)
admin.site.register(PrazoPagamento)
admin.site.register(Cliente)
