# Generated by Django 4.1.7 on 2023-05-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_alter_consult_lng'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='lat',
            field=models.FloatField(default=10.606656),
            preserve_default=False,
        ),
    ]
