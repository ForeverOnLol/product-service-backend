from django.contrib import admin
from .models import Catalog, Product


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')



admin.site.register([Catalog, Product])
