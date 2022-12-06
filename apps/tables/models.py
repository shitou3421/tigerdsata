from django.db import models

from apps.config.models import ColumnTypeModel
from apps.project.models import VersionModel


class Table(models.Model):
    name = models.CharField(verbose_name="表名", help_text="表名", max_length=100)
    raw_table_name = models.CharField(verbose_name="原库中表名", help_text="原库中表名", max_length=100)
    parent_table_id = models.ForeignKey("self", on_delete=models.SET_NULL, default=None, null=True, blank=True,
                                        verbose_name="父级表",
                                        help_text="父级表", related_name="t_table")
    version = models.ForeignKey(VersionModel, on_delete=models.SET_NULL, null=True, default=None, verbose_name="版本",
                                related_name="v_table")

    class Meta:
        db_table = "table_table"
        verbose_name = "表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(verbose_name="字段名", help_text="字段名", max_length=100)
    raw_column_name = models.CharField(verbose_name="原表中字段名", help_text="原表中字段名", max_length=100)
    type = models.ForeignKey(ColumnTypeModel, on_delete=models.SET_NULL, null=True, default=None, blank=True, verbose_name="字段类型",
                             help_text="字段类型", related_name="c_type")
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, default=None, blank=True, verbose_name="表",
                              help_text="表", related_name="t_column")
    version = models.ForeignKey(VersionModel, on_delete=models.SET_NULL, null=True, default=None,
                                verbose_name="版本",
                                related_name="v_column")

    class Meta:
        db_table = "table_column"
        verbose_name = "字段"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
