from django.contrib import admin

from .models import (
    Casts, 
    Directors, 
    MainActor, 
    Movies, 
    Screenwriters,
    Villains
)


@admin.register(Casts)
class CastsAdmin(admin.ModelAdmin):
    list_display = ("name", "birthday")


@admin.register(Villains)
class VillainsAdmin(admin.ModelAdmin):
    list_display = ("character_name", "name", "birthday")


@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    list_display = ("name", "birthday")


@admin.register(Screenwriters)
class ScreenwritersAdmin(admin.ModelAdmin):
    list_display = ("name", "birthday")


@admin.register(MainActor)
class MainActorAdmin(admin.ModelAdmin):
    list_display = ("character_name", "name", "birthday")


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published_year",
        "synopsis",
        "imdb_evaluation",
    )
