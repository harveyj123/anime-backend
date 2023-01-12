# Generated by Django 4.1.3 on 2022-12-21 05:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anime', '0007_remove_anime_aired_remove_anime_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatedAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('anime_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
            ],
        ),
        migrations.CreateModel(
            name='MostSearchedAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily', models.ManyToManyField(related_name='daily2Anime', to='anime.anime')),
                ('monthly', models.ManyToManyField(related_name='monthly2Anime', to='anime.anime')),
                ('weekly', models.ManyToManyField(related_name='weekly2Anime', to='anime.anime')),
                ('yearly_searched', models.ManyToManyField(related_name='yearly2Anime', to='anime.anime')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('most_searched_anime', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history.mostsearchedanime')),
                ('rated_anime', models.ManyToManyField(to='history.ratedanime')),
            ],
        ),
    ]