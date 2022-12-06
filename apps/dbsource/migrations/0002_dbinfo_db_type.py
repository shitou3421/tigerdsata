# Generated by Django 4.0.5 on 2022-06-29 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_dbtypemodel'),
        ('dbsource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbinfo',
            name='db_type',
            field=models.ForeignKey(blank=True, default=None, help_text='数据库类型', null=True, on_delete=django.db.models.deletion.SET_NULL, to='config.dbtypemodel', verbose_name='数据库类型'),
        ),
    ]