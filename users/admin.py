from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Профили"
    fields = ("sex", "birthdate")


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = (
        "username", "email", "first_name", "last_name", "get_sex", "get_birthdate"
    )

    def get_sex(self, obj):
        return obj.userprofile.sex
    get_sex.admin_order_field = "userprofile__sex"
    get_sex.short_description = "Пол"

    def get_birthdate(self, obj):
        return obj.userprofile.birthdate
    get_birthdate.admin_order_field = "userprofile__birthdate"
    get_birthdate.short_description = "Дата рождения"

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("sex", "birthdate")}),
    )  # type: ignore
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("sex", "birthdate")})
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


