from django.contrib import admin
from .models import Adoption, Package


class AdoptionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'animal',
        'animal_plural',
        'date_added',
    )

    readonly_fields = ('date_added',)

    fields = (
        'animal', 'animal_plural', 'desc',
        'image_url', 'image',
        'image_header_url', 'image_header',
        'date_added',
    )

    ordering = (
        'pk',
    )


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'friendly_name',
        'name',
        'adoption',
        'price',
    )

    fields = (
        'adoption', 'sku', 'name', 'friendly_name',
        'desc', 'price', 'image_url', 'image',
    )

    readonly_fields = ('sku',)

    ordering = (
        'sku',
    )


admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(Package, PackageAdmin)
