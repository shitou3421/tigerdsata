from django.contrib import admin
from django.db.models import QuerySet

from apps.tables.models import Table, Column


class ColumnInlineAdmin(admin.StackedInline):
    model = Column
    extra = 1


class TableAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "raw_table_name", "parent_table_id", "version")
    list_display_links = ("name",)
    list_filter = ("name", "version")
    list_per_page = 10

    inlines = [ColumnInlineAdmin]

    actions = ['set_version']

    @admin.action(description="批量设置版本号")
    def set_version(self, request, queryset: QuerySet):
        """
        """
        # todo: 需要编写前端中间页面



class ColumnAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "raw_column_name", "type", "table", "version")
    list_display_links = ("name",)
    list_filter = ("name",)
    list_editable = ("raw_column_name", "type", "table")
    list_per_page = 10



admin.site.register(Table, TableAdmin)
admin.site.register(Column, ColumnAdmin)
