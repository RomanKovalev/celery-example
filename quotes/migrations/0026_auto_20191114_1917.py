# Generated by Django 2.2.5 on 2019-11-15 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0025_auto_20191114_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_as_qotd',
            field=models.BooleanField(default=False, verbose_name='Has Been QOTD'),
        ),
    ]
