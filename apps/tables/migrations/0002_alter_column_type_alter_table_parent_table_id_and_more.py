# Generated by Django 4.0.5 on 2022-06-29 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('config', '0001_initial'),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='type',
            field=models.ForeignKey(default=None, help_text='字段类型', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_type', to='config.columntypemodel', verbose_name='字段类型'),
        ),
        migrations.AlterField(
            model_name='table',
            name='parent_table_id',
            field=models.ForeignKey(default=None, help_text='父级表', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='t_table', to='tables.table', verbose_name='父级表'),
        ),
        migrations.AlterField(
            model_name='table',
            name='version',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='v_table', to='project.versionmodel', verbose_name='版本'),
        ),
    ]