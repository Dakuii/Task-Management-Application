# Generated by Django 3.2.18 on 2023-06-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20230620_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='image',
            field=models.ImageField(upload_to='worskpace_images/'),
        ),
    ]
