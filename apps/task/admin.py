import json

from django.contrib import admin
from django.db.models import QuerySet

from apps.task.models import TaskModel
from db_driver.db_server import DBServer


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "version", "db")
    list_display_links = ("name",)
    list_filter = ("name", "status", "version", "db")
    list_per_page = 10
    actions = ["execute"]

    @admin.action(description="执行任务")
    def execute(self, request, queryset: QuerySet):
        for q in queryset:
            sql_list = eval(q.sql)
            db_url = q.db.get_db_driver()
            print(db_url)
            db = DBServer().init(q.db.db_type.name, db_url)
            res = self.do_sql(db, queryset, sql_list)
            if res:
                queryset.update(status="3")
            else:
                queryset.update(status="4")

    def do_sql(self, db, queryset, sql_list):
        for sql in sql_list:
            try:
                db.save(sql)
            except Exception as e:
                print(sql)
                RuntimeError("执行sql出错", e)
                return False
        return True


admin.site.register(TaskModel, TaskAdmin)
