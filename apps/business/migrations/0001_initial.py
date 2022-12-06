# Generated by Django 4.0.5 on 2022-06-29 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='业务名称', max_length=100, verbose_name='业务名称')),
                ('parent_business_id', models.ForeignKey(help_text='父业务', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='b_business', to='business.business', verbose_name='父业务')),
                ('tables', models.ManyToManyField(help_text='业务表', related_name='t_business', to='tables.table', verbose_name='业务表')),
            ],
            options={
                'verbose_name': '业务',
                'verbose_name_plural': '业务',
                'db_table': 'business',
            },
        ),
    ]
