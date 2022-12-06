# Generated by Django 4.0.5 on 2022-06-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SqlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sql', models.TextField(help_text='执行sql', verbose_name='执行sql')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '项目版本',
                'verbose_name_plural': '项目版本',
                'db_table': 'sql_sql',
            },
        ),
    ]