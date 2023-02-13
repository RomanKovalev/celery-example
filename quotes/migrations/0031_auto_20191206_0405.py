# Generated by Django 2.2.7 on 2019-12-06 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0030_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, unique=True),
        ),
    ]
