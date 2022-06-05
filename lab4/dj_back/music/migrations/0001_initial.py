# Generated by Django 4.0.5 on 2022-06-05 16:35

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя автора')),
                ('year', models.IntegerField(null=True, validators=[music.models.is_positive], verbose_name='Год рождения')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название трека')),
                ('year', models.IntegerField(null=True, validators=[music.models.is_positive], verbose_name='Год выпуска')),
                ('author', models.ManyToManyField(to='music.author')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
            },
        ),
    ]
