# Generated by Django 4.0.3 on 2022-03-14 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_event_hiring'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiring',
            old_name='decription',
            new_name='description',
        ),
    ]
