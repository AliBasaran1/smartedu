# Generated by Django 3.1.5 on 2024-11-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Tag'),
        ),
    ]
