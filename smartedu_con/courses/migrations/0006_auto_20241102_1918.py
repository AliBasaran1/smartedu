# Generated by Django 3.1.5 on 2024-11-02 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='tags',
            new_name='tag',
        ),
    ]
