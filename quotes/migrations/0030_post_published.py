# Generated by Django 2.2.7 on 2019-11-21 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0029_remove_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
