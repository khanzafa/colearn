# Generated by Django 4.2.5 on 2023-12-04 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_alter_material_file_materialhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(upload_to='materials/uploads/'),
        ),
    ]
