from django.contrib import admin
from .models import Adoption


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
        'image_url', 'image', 'date_added',
    )

    ordering = (
        'pk',
    )


admin.site.register(Adoption, AdoptionAdmin)
