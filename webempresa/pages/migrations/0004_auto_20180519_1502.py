# Generated by Django 2.0.5 on 2018-05-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180519_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
    ]
