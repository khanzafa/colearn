# Generated by Django 4.2.5 on 2023-12-10 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_rename_view_visit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='user',
            new_name='author',
        ),
    ]
