from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_admin', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_admin', 'is_admin']
    search_fields = ['username']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.data.get('password'))
            obj.created_by = request.user
            obj.updated_by = request.user

        elif len(form.changed_data) != 0:
            if 'password' in form.changed_data:
                obj.set_password(form.data.get('password'))

            obj.updated_by = request.user
        obj.save()


admin.site.register(User, UserAdmin)
