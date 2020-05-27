# Generated by Django 2.2.12 on 2020-05-25 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('a_text', models.TextField(verbose_name='Текст Статьи')),
                ('pud_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('c_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('c_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]