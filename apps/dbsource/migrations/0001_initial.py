# Generated by Django 4.0.5 on 2022-06-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(help_text='主机/域名', max_length=100, verbose_name='主机/域名')),
                ('port', models.CharField(help_text='端口', max_length=10, verbose_name='端口')),
                ('username', models.CharField(help_text='用户名', max_length=100, verbose_name='用户名')),
                ('password', models.CharField(help_text='密码', max_length=100, verbose_name='密码')),
            ],
            options={
                'verbose_name': '数据库信息',
                'verbose_name_plural': '数据库信息',
                'db_table': 'dbsource_dbinfo',
            },
        ),
    ]
