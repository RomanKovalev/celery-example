# Generated by Django 2.2.7 on 2019-11-21 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0028_quotecollections_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
    ]
