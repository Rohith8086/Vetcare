# Generated by Django 4.1.7 on 2023-05-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_consult_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='lat',
            field=models.FloatField(),
        ),
    ]