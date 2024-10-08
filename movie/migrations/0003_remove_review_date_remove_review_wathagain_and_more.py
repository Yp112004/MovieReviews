# Generated by Django 5.1 on 2024-09-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_description_alter_movie_title_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date',
        ),
        migrations.RemoveField(
            model_name='review',
            name='wathAgain',
        ),
        migrations.AddField(
            model_name='review',
            name='watchAgain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(),
        ),
    ]
