from django.contrib import admin
from .models import qr_generator

@admin.register(qr_generator)
class QRGeneratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'generated_by', 'created_at', 'updated_at')
    search_fields = ('name', 'generated_by__username')
    list_filter = ('created_at', 'updated_at', 'generated_by')
    readonly_fields = ("generated_by",)
    

