# Register your models here.
from django.contrib import admin, messages
from django.db.models import QuerySet
from django.utils.translation import ngettext

from apps.business.models import Business, BusinessWork
from apps.config.models import ColumnTypeModel, RolesModel
from apps.tables.models import Column
from apps.task.models import TaskModel
from generater_data.roles_type_func import RolesTypeFunc

from db_driver.base_db import BaseDB


class BusinessAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "version")
    list_display_links = ("name",)
    # list_editable = ("parent_business_id",)
    list_per_page = 10


class BusinessWorkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "num", "db", "version")
    list_display_links = ("name",)
    list_editable = ("num", "db", "version")
    list_per_page = 10
    actions = ["create_sql"]

    @admin.action(description="生成sql与任务")
    def create_sql(self, request, queryset: QuerySet):

        rtf = RolesTypeFunc()
        for q in queryset:
            nums = q.num  # 获取执行次数
            business = q.business.all()
            buss_dict = {}
            sql_list = []

            for i in range(nums):
                for b in business:
                    bus_dict = {}
                    b_name = b.name
                    tables = b.tables.all()
                    for t in tables:  # 'lecturer_20220701092921_copy'
                        table_name = t.raw_table_name  # table_name重复的情况处理
                        columns = Column.objects.filter(table__raw_table_name=table_name)

                        # table_map = list(zip(columns.values_list('raw_column_name', flat=True),
                        #                      columns.values_list('type__code', flat=True)))

                        code_value_list = []
                        code_list = columns.values_list('type__code', flat=True)
                        para_list = columns.values_list('type__para', flat=True)
                        for code, para in zip(code_list, para_list):
                            print(code.__repr__() + para.__repr__())
                            if para is None:
                                code_value_list.append(rtf.get(code, para))
                            else:
                                code_value_list.append(rtf.get(code, **para))
                        column_list = list(zip(columns.values_list('raw_column_name', flat=True), code_value_list))
                        sql_list.append(BaseDB.format_mysql_sql(table_name, column_list))
                        bus_dict.update({(b_name, table_name, i + 1): column_list})

                    buss_dict.update(bus_dict)
            TaskModel.objects.create(
                name=q.name, sql=sql_list, version=q.version, db=q.db)
        self.message_user(request, "创建成功", messages.SUCCESS)


admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessWork, BusinessWorkAdmin)
