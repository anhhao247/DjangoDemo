# Generated by Django 5.1.6 on 2025-02-26 02:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='courses/%Y/%m/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoapp.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='lessons/%Y/%m/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoapp.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
