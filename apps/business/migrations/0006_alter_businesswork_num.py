# Generated by Django 4.0.5 on 2022-06-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_alter_businesswork_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesswork',
            name='num',
            field=models.IntegerField(default=1, help_text='执行次数, 默认1次', verbose_name='执行次数'),
        ),
    ]