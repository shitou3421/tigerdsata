import datetime

from django.contrib import admin, messages
from django.db.models import QuerySet

from apps.config.models import ColumnTypeModel
from apps.dbsource.models import DbInfo
from apps.tables.models import Table, Column
from db_driver.driver import get_db_columns_type


class DbsourceDbInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "host", "port", "username", 'db_type', 'init_db')
    list_display_links = ("id",)
    list_filter = ("host", 'db_type', "name", "db_type")
    list_per_page = 10
    list_editable = ("name", "host", "port", "username", "db_type", 'init_db')

    actions = ["import_db"]

    @admin.action(description="导入系统")
    def import_db(self, request, queryset: QuerySet):
        for i in queryset:
            url = i.get_db_driver()
            print(url)
            db_dict = get_db_columns_type(url)
            print(db_dict)

            for table_name, columns in db_dict.items():
                table_obj = Table.objects.create(
                    name=table_name+ "_" + datetime.datetime.strftime(datetime.datetime.today(), "%Y%m%d%H%M%S") + "_copy",
                    raw_table_name=table_name,
                    # version=i.version+"_copy"
                )
                for column, column_type in columns.items():
                    code = column_type.lower()
                    print(code)
                    ct = ColumnTypeModel.objects.get(code=code)
                    Column.objects.create(
                        name=column + "_" + datetime.datetime.strftime(datetime.datetime.today(), "%Y%m%d%H%M%S") + "_copy",
                        raw_column_name=column,
                        type=ct,
                        table=table_obj,
                        # version=i.version+"_copy"
                    )
        self.message_user(request, "创建成功", messages.SUCCESS)


admin.site.register(DbInfo, DbsourceDbInfoAdmin)
