from django.db import models

from generater_data.RoleEnum import RoleEnum


class DbTypeModel(models.Model):
    name = models.CharField(verbose_name="数据库类型", max_length=100)

    class Meta:
        db_table = "config_db_type"
        verbose_name = "支持数据库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


CODE = [(v.name, v.value) for v in RoleEnum]


class ColumnTypeModel(models.Model):
    name = models.CharField(verbose_name="字段类型名称", help_text="字段类型名称", default=None, null=True, blank=True,
                            max_length=100)

    code = models.CharField(max_length=100, verbose_name="字段类型编码", help_text="字段类型编码", choices=CODE, default=None,
                            null=True, blank=True)

    para = models.JSONField(max_length=100, verbose_name="参数", help_text="参数", blank=True)

    class Meta:
        db_table = "config_column_type"
        verbose_name = "字段类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class RoleTypeModel(models.Model):
#     name = models.CharField(verbose_name="规则名称", help_text="规则名称", default=None, null=True, blank=True, max_length=100)
#
#     class Meta:
#         db_table = "config_roleType"
#         verbose_name = "公共规则设置"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


class RolesModel(models.Model):
    # name = models.ForeignKey(RoleTypeModel, on_delete=models.SET_NULL, default=None, null=True, blank=True,
    #                          verbose_name="规则名称", help_text="规则名称", related_name="rt_role")
    name = models.CharField(default=None, null=True, blank=True, max_length=300,
                            verbose_name="规则名称", help_text="规则名称")

    role = models.CharField(verbose_name="具体规则", help_text="具体规则",
                            max_length=300, default=None, null=True, blank=True)

    column = models.ForeignKey(ColumnTypeModel, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                               verbose_name="规则字段", help_text="规则字段", related_name="c_column")

    class Meta:
        db_table = "config_role"
        verbose_name = "字段规则"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_role(self):
        return self.role


class TableContentModel(models.Model):
    arg_code = models.CharField(verbose_name="编码", help_text="字段类型", max_length=100)
    arg_name = models.CharField(verbose_name="名称", help_text="名称", max_length=100)
    value_generate = models.CharField(verbose_name="值生成器", help_text="值生成器", max_length=100)

    class Meta:
        db_table = "config_table_content"
        verbose_name = "表上下文"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.arg_name

# class GenerateTypeModel(models.Model):
#     name = models.CharField(verbose_name="插入类型", help_text="插入类型", max_length=100)
#
#     class Meta:
#         db_table = "config_generate_type"
#         verbose_name = "生成类型"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


# TASKSTATUSCHOICE = (
#     (1, "未执行"),
#     (2, "进行中"),
#     (3, "成功"),
#     (4, "失败"),
# )
#
#
# class TaskStatusModel(models.Model):
#     name = models.CharField(choices=TASKSTATUSCHOICE, default=1, verbose_name="任务状态", help_text="任务状态", max_length=100)
#
#     class Meta:
#         db_table = "config_task_status"
#         verbose_name = "任务状态"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
