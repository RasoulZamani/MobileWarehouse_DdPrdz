from django.contrib import admin
from .models import Mobile
# Register your models here.
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    search_fields=('brand','nationality','model',
                   'price','color',
                   'country')
    list_filter = ('brand','nationality','model',
                   'price','color','screen_size',
                   'country','available')