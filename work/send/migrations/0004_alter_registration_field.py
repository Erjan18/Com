# Generated by Django 4.0.1 on 2022-01-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0003_registration_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='field',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
    ]