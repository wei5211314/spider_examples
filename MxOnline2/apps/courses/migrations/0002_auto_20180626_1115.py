# Generated by Django 2.0.1 on 2018-06-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=models.TextField(verbose_name='课程详情'),
        ),
    ]