from django.contrib import admin, messages
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from store import models
from store.models import Product, Customer, Collection, ProductImage

INVENTORY_THRESHOLD = 10
LOW = 'Low'
OK = 'OK'


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    LOW_INVENTORY = f'<{INVENTORY_THRESHOLD}'
    OK_INVENTORY = f'>={LOW_INVENTORY}'

    def lookups(self, request, model_admin):
        return [
            (self.LOW_INVENTORY, LOW),
            (self.OK_INVENTORY, OK)
        ]

    def queryset(self, request, queryset):
        if self.value() == self.LOW_INVENTORY:
            return queryset.filter(inventory__lt=INVENTORY_THRESHOLD)
        elif self.value() == self.OK_INVENTORY:
            return queryset.filter(inventory__gte=INVENTORY_THRESHOLD)
        return queryset


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    inlines = [ProductImageInline]
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title']

    def collection_title(self, product: Product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product: Product):
        if product.inventory < INVENTORY_THRESHOLD:
            return LOW
        return OK

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.SUCCESS
        )

    class Media:
        css = {
            'all': ['store/styles.css']
        }


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders_count(self, customer: Customer):
        url = (
                reverse('admin:store_order_changelist')
                + '?'
                + urlencode({'customer__id': str(customer.id)})
        )
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count=Count('order'))


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection: Collection):
        url = (
                reverse('admin:store_product_changelist')
                + '?'
                + urlencode({'collection__id': str(collection.id)})
        )
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('products'))


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    min_num = 1
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']
