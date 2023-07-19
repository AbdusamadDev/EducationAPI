# Generated by Django 4.2 on 2023-07-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('course_name', models.CharField(max_length=256, verbose_name='Course Name')),
                ('study_type', models.CharField(max_length=256, verbose_name='Study Type')),
                ('course_year', models.CharField(max_length=256, verbose_name='Course Year')),
                ('course_language', models.CharField(max_length=256, verbose_name='Course Language')),
                ('file01', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file02', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file03', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file04', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file05', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file06', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file07', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file08', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file09', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file10', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file11', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file12', models.FileField(upload_to='applications/%Y/%m/%d')),
                ('file13', models.FileField(upload_to='applications/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
            },
        ),
    ]