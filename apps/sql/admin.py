from django.contrib import admin

from apps.sql.models import SqlModel


class SqlAdmin(admin.ModelAdmin):
    list_display = ("sql", "create_time")


admin.site.register(SqlModel, SqlAdmin)
