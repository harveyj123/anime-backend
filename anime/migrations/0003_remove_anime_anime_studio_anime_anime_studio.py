# Generated by Django 4.1.3 on 2022-12-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_studio_rename_studio_anime_anime_studio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='anime_studio',
        ),
        migrations.AddField(
            model_name='anime',
            name='anime_studio',
            field=models.ManyToManyField(to='anime.studio'),
        ),
    ]