# Generated by Django 3.0.8 on 2020-07-24 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0010_remove_dish_calories_sum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиент'},
        ),
    ]
