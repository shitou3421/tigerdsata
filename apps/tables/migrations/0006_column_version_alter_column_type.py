# Generated by Django 4.0.5 on 2022-06-29 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_alter_rolesmodel_options_remove_columntypemodel_role_and_more'),
        ('project', '0002_remove_projectmodel_version_versionmodel_project'),
        ('tables', '0005_remove_column_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='version',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='v_column', to='project.versionmodel', verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='column',
            name='type',
            field=models.ForeignKey(blank=True, default=None, help_text='字段类型', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_type', to='config.columntypemodel', verbose_name='字段类型'),
        ),
    ]
