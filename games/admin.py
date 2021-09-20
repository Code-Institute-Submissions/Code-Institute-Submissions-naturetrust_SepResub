from django.contrib import admin
from .models import Game, Edition, Section, Content


class EditionInlineAdmin(admin.TabularInline):
    model = Edition

    readonly_fields = ('sku',)

    fields = (
        'name', 'friendly_name',
        'friendly_name_full', 'desc',
        'helper_text', 'sku', 'price',
    )

    extra = 0


class SectionInlineAdmin(admin.TabularInline):
    model = Section
    extra = 0


class ContentInlineAdmin(admin.TabularInline):
    model = Content
    extra = 0


class GameAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'pk',
        'publisher',
        'developer',
        'date_added',
    )

    inlines = (
        EditionInlineAdmin,
        SectionInlineAdmin,
        ContentInlineAdmin,
    )

    readonly_fields = ('date_added',)

    fields = (
        'friendly_name', 'name', 'url_name', 'publisher',
        'publisher_friendly_name', 'developer',
        'description', 'image_url', 'image',
        'date_added',
    )

    ordering = (
        'pk',
    )


admin.site.register(Game, GameAdmin)
