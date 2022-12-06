from django.db import models


class ProjectModel(models.Model):
    name = models.CharField(verbose_name="项目名称", help_text="项目名称", max_length=300)

    class Meta:
        db_table = "project_project"
        verbose_name = "项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VersionModel(models.Model):
    name = models.CharField(verbose_name="版本名称", help_text="版本名称", max_length=300)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                                verbose_name="版本", related_name="v_project")

    class Meta:
        db_table = "project_version"
        verbose_name = "项目版本"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
