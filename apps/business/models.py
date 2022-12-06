from django.db import models

from apps.dbsource.models import DbInfo
from apps.project.models import VersionModel
from apps.tables.models import Table


class Business(models.Model):
    name = models.CharField(verbose_name="业务名称", help_text="业务名称", max_length=100)
    parent_business_id = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, default=None, blank=True,
                                           verbose_name="父业务", help_text="父业务",
                                           related_name="b_business")
    tables = models.ManyToManyField(Table, verbose_name="业务表", help_text="业务表", related_name="t_business")
    version = models.ForeignKey(VersionModel, on_delete=models.SET_NULL, null=True, default=None, verbose_name="版本",
                                related_name="v_business")
    class Meta:
        db_table = "business"
        verbose_name = "业务配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BusinessWork(models.Model):
    name = models.CharField(verbose_name="名称", help_text="名称", max_length=100, default=None, null=True, blank=True)
    business = models.ManyToManyField(Business, verbose_name="包含业务", help_text="包含业务", related_name="b_business_work")
    num = models.IntegerField(verbose_name="执行次数", help_text="执行次数, 默认1次", default=1)
    version = models.ForeignKey(VersionModel, on_delete=models.SET_NULL, null=True, default=None, verbose_name="版本",
                                related_name="v_business_work")
    db = models.ForeignKey(DbInfo, on_delete=models.SET_NULL, default=None, blank=True, null=True,
                           verbose_name="执行的数据库", help_text="执行的数据库", related_name="db_business_work")

    class Meta:
        db_table = "business_work"
        verbose_name = "工作配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
