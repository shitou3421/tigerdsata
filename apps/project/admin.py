from django.contrib import admin
from django.db.models import QuerySet

from apps.project.models import ProjectModel, VersionModel

class VersionInlineAdmin(admin.StackedInline):
    model = VersionModel
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 10
    inlines = [VersionInlineAdmin]



class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 10
    actions = ["copy_version"]

    @admin.action(description="复制版本")
    def copy_version(self, request, queryset: QuerySet):
        pass



admin.site.register(ProjectModel, ProjectAdmin)
admin.site.register(VersionModel, VersionAdmin)

admin.site.site_header = "数据管理系统"
admin.site.site_title = "数据管理系统"

