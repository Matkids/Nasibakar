from django.contrib import admin
from .models import MenuItem, Order, OrderItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'deskripsi')
    search_fields = ('nama',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tanggal_pesan', 'status')
    list_filter = ('status',)
    search_fields = ('user__username',)

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
