from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = (
        'name',
        '_type',
        'price',
    )


