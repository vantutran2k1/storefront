from django.contrib import admin

from store import models

# Register your models here.
admin.site.register(models.Collection)
admin.site.register(models.Product)
