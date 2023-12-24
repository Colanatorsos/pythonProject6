from django.contrib import admin

from app_account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone_number",
        "created_at",
    )
    search_fields = ("username", "email", "phone_number", "created_at")
    # list_filter = ("created_at")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "username",
                    "full_name",
                    "is_verified",
                    "is_active",
                    "created_at",
                )
            },
        ),
        # ("Permissions", {"fields": ("is_staff",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "full_name",
                    "phone_number",
                ),
            },
        ),
    )
    readonly_fields = ("created_at",)


admin.site.register(User, UserAdmin)