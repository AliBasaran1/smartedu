# Generated by Django 3.1.5 on 2024-11-02 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20241102_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='tag',
            new_name='tags',
        ),
    ]
