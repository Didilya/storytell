from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import UserCreationForm, UserChangeForm
from users.models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        "profile_name",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_admin",
    ]
    list_filter = ["is_admin", "is_active"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["profile_name", "first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_admin"]}),
        ("Photo", {"fields": ["thumbnail"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "profile_name",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "thumbnail",
                ],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
