# Generated by Django 3.2.18 on 2023-05-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbookapp', '0002_recipes_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]