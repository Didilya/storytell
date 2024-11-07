from django.contrib import admin
from core import models


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["id", "uid", "user", "text", "created", "modified"]
    search_fields = ["user__email"]
    empty_value_display = "-"
    exclude = ["created", "modified"]


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "uid", "title", "created", "modified"]
    search_fields = ["user__email"]
    empty_value_display = "-"
    exclude = ["created", "modified"]


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "entry", "is_good", "is_bad", "created"]
    search_fields = ["entry__user__email"]
    empty_value_display = "Null"
    exclude = ["created"]


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "entry", "created"]
    search_fields = ["entry__user__email"]
    empty_value_display = "Null"
    exclude = ["created"]
