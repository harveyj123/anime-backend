# Generated by Django 4.1.5 on 2023-01-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_user_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_anime',
            field=models.ManyToManyField(blank=True, related_name='taken', to='users.useranime'),
        ),
    ]