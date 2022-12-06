from django.contrib import admin

from apps.config.models import ColumnTypeModel, RolesModel, DbTypeModel


class DbTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 10


class RolesInlineAdmin(admin.StackedInline):
    model = RolesModel
    extra = 1

class ColumnTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    list_display_links = ("name",)
    list_filter = ("name", "code")
    list_per_page = 10

    # inlines = [RolesInlineAdmin]

class GenerateTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 10


class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 10


class RolesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role")
    list_display_links = ("name",)
    list_filter = ("name", "role")
    list_per_page = 10

admin.site.register(ColumnTypeModel, ColumnTypeAdmin)
# admin.site.register(GenerateTypeModel, GenerateTypeAdmin)
# admin.site.register(TaskStatusModel, TaskStatusAdmin)
admin.site.register(DbTypeModel, DbTypeAdmin)
# admin.site.register(RolesModel, RolesAdmin)
