from django.contrib import admin
from .models import Game, Edition, Section, Content


class EditionInlineAdmin(admin.TabularInline):
    model = Edition
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
        'friendly_name', 'name', 'publisher',
        'publisher_friendly_name', 'developer',
        'description', 'image_url', 'image',
        'date_added',
    )

    ordering = (
        'pk',
    )


admin.site.register(Game, GameAdmin)
