from django.contrib import admin

# Register your models here.

# plan
from .models import Transaction
# admin.site.register(Transaction)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('client', 'action', 'shares', 'symbol',  'status', 'created_at')
    list_filter = ('status', 'action', 'created_at', 'client')
    search_fields = ('client', 'symbol')
    date_hierarchy = 'created_at'
    ordering = ('status', 'created_at')