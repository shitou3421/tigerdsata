from django.db import models

# from apps.config.models import GenerateTypeModel, TaskStatusModel
from apps.dbsource.models import DbInfo
from apps.project.models import VersionModel

TASKSTATUSCHOICE = (
    ("1", "未执行"),
    ("2", "进行中"),
    ("3", "成功"),
    ("4", "失败"),
)


class TaskModel(models.Model):
    name = models.CharField(verbose_name="任务名称", help_text="任务名称", max_length=300, default=None, blank=True, null=True)
    sql = models.TextField(verbose_name="sql语句", help_text="sql语句", default=None, blank=True, null=True)
    status = models.CharField(choices=TASKSTATUSCHOICE, default="1", verbose_name="任务状态", help_text="任务状态",
                              max_length=100)
    version = models.ForeignKey(VersionModel, on_delete=models.SET_NULL, null=True, default=None, verbose_name="版本",
                                help_text="版本",
                                related_name="v_task")
    db = models.ForeignKey(DbInfo, on_delete=models.SET_NULL, default=None, blank=True, null=True,
                           verbose_name="执行的数据库", help_text="执行的数据库", related_name="db_task")

    class Meta:
        db_table = "task_task"
        verbose_name = "任务配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
