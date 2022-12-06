# Generated by Django 4.0.5 on 2022-06-29 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VersionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='版本名称', max_length=300, verbose_name='版本名称')),
            ],
            options={
                'verbose_name': '项目版本',
                'verbose_name_plural': '项目版本',
                'db_table': 'project_version',
            },
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=300, verbose_name='项目名称')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='v_project', to='project.versionmodel', verbose_name='版本')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'project_project',
            },
        ),
    ]