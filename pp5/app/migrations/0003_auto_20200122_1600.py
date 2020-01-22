# Generated by Django 3.0.2 on 2020-01-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.TextField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.URLField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=None, max_length=100),
        ),
    ]