# Generated by Django 4.1.7 on 2023-02-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0014_anime_number_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='number_rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]