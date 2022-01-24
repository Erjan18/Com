# Generated by Django 4.0.1 on 2022-01-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='category',
            field=models.CharField(choices=[('Очно', 'Очно'), ('Заочно', 'Заочно'), ('Дистанционно', 'Дистанционно'), ('Слушатель', 'Слушатель'), ('Докладчик', 'Докладчик')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='country',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='mail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='number',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='organization',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='position',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(choices=[('Физическое лицо', 'Физическое лицо'), ('Юридическое лицо', 'Юридическое лицо')], max_length=50, null=True),
        ),
    ]