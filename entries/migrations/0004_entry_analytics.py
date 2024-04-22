# Generated by Django 5.0.2 on 2024-03-18 13:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_delete_mymodel_entry_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry_Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]