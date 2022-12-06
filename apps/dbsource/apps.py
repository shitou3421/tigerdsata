from django.apps import AppConfig


class DbsourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.dbsource'
    verbose_name = "数据源配置"
