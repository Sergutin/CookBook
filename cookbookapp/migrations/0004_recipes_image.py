# Generated by Django 3.2.18 on 2023-05-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbookapp', '0003_recipes_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images'),
        ),
    ]
