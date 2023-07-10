# Generated by Django 4.2.2 on 2023-07-04 09:57

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=base.models.image_upload_path),
        ),
    ]