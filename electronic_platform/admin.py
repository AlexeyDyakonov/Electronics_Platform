from django.contrib import admin, messages
from django.utils.html import format_html

from electronic_platform.models import Supplier, Product, Contact


@admin.action(
    description="Очистить задолженность перед поставщиком у выбранных объектов"
)
def debt_clear(self, request, queryset):
    count = queryset.update(debt=0.00)
    self.message_user(
        request, f"{count} задолженности были успешно очищены.", messages.WARNING
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "provider",
        "provider_type",
        "level",
        "debt",
        "creation_time",
    )
    readonly_fields = ("provider_link",)
    list_filter = ("contact__city",)
    actions = [debt_clear]

    def provider_link(self, obj):
        if obj.provider:
            url = f"/admin/online_platform/provider/{obj.provider.id}/change/"
            return format_html(f'<a href="{url}">{obj.provider.name}</a>')
        return "-"

    provider_link.short_description = "Ссылка на поcтавщика"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "model",
        "release_date",
        "provider",
    )
    search_fields = ("title",)
    list_filter = (
        "release_date",
        "provider",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "provider",
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )
    search_fields = ("email",)
    list_filter = ("city",)
