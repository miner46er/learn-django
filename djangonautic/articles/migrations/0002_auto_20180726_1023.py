# Generated by Django 2.0.7 on 2018-07-26 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='title',
        ),
    ]
