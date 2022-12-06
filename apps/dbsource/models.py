from django.db import models

from apps.config.models import DbTypeModel


class DbInfo(models.Model):
    name = models.CharField(verbose_name="数据库名字", help_text="数据库名字", max_length=100, null=True, blank=True,
                            default=None)
    host = models.CharField(verbose_name="主机/域名", help_text="主机/域名", max_length=100)
    port = models.CharField(verbose_name="端口", help_text="端口", max_length=10)
    username = models.CharField(verbose_name="用户名", help_text="用户名", max_length=100)
    password = models.CharField(verbose_name="密码", help_text="密码", max_length=100)
    db_type = models.ForeignKey(DbTypeModel, on_delete=models.SET_NULL, null=True,
                                verbose_name="数据库类型", help_text="数据库类型")
    init_db = models.CharField(verbose_name="初始连接数据库", help_text="初始连接数据库", max_length=300, default=None, null=True)

    class Meta:
        db_table = "dbsource_dbinfo"
        verbose_name = "数据库信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_db_driver(self):
        driver_url = self.db_type.name + "://" + self.username + ":" + self.password + "@" + self.host + ":" + self.port + "/" + self.init_db
        return driver_url
