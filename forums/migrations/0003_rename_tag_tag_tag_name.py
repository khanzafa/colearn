# Generated by Django 4.2.5 on 2023-12-10 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='tag_name',
        ),
    ]
