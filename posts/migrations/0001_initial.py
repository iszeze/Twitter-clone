# Generated by Django 3.2.7 on 2022-03-29 21:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create DateTime')),
                ('image', cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, null=True, verbose_name='image')),
                ('likes', models.IntegerField(blank=True, default=0, verbose_name='likes')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
