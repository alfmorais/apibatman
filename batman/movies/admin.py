from django.contrib import admin

from .models import Cast, Movies, Villain


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "main_actor",
        "director",
        "casts",
        "villains",
        "summary",
        "published",
    )


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "birthday",
        "demise",
        "height",
    )


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "birthday",
        "demise",
        "height",
    )
