from django.db import models

from apps.project.models import VersionModel


class SqlModel(models.Model):
    sql = models.TextField(verbose_name="执行sql", help_text="执行sql")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text="创建时间")

    version = models.ForeignKey(VersionModel, on_delete=models.SET_NULL, null=True, default=None, verbose_name="版本",
                                related_name="v_sql_log")

    class Meta:
        db_table = "sql_log"
        verbose_name = "历史记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sql
