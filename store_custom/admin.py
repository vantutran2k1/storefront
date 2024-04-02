from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from store.models import Product
from tags.models import TaggedItem


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    search_fields = ['title']


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
