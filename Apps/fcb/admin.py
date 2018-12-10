from django.contrib import admin
from Apps.fcb.models import News, Player
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','large_img','small_img','source','content','type']

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_by = request.user
            obj.updated_by = request.user

        elif len(form.changed_data) != 0:
            obj.updated_by = request.user
        obj.save()

admin.site.register(News,NewsAdmin)
admin.site.register(Player)