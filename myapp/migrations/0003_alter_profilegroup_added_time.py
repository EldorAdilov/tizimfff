# Generated by Django 5.1.1 on 2025-02-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_video_description_remove_video_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilegroup',
            name='added_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
