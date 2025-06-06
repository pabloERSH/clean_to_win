# Generated by Django 5.1.1 on 2024-11-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Никнейм пользователя')),
                ('avatar_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='Путь к аватарке')),
                ('short_msg', models.CharField(default='Отзыв', max_length=40, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
