# Generated by Django 5.1.1 on 2025-02-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.RemoveField(
            model_name='video',
            name='group',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
        migrations.RemoveField(
            model_name='video',
            name='youtube_url',
        ),
        migrations.AddField(
            model_name='video',
            name='groups',
            field=models.ManyToManyField(blank=True, to='myapp.group'),
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_link',
            field=models.URLField(default='Null'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
