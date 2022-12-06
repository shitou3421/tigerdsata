from django.apps import AppConfig


class SqlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sql'
    verbose_name = "执行SQL记录"
