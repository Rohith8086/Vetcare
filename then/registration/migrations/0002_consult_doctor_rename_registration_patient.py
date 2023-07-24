# Generated by Django 4.1.7 on 2023-05-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('pet_name', models.CharField(max_length=250)),
                ('pet_age', models.IntegerField()),
                ('pet_type', models.CharField(max_length=250)),
                ('symptoms', models.TextField()),
                ('doctor', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'consult',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('phonenumber', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('filename', models.FileField(upload_to='doc_certificates')),
                ('time1', models.TimeField(blank=True)),
                ('time2', models.TimeField(blank=True)),
                ('days', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Registration',
            new_name='Patient',
        ),
    ]