# Generated by Django 4.0.5 on 2022-06-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_business_version_businesswork_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesswork',
            name='business',
            field=models.ManyToManyField(help_text='包含业务', related_name='b_business_work', to='business.business', verbose_name='包含业务'),
        ),
    ]
