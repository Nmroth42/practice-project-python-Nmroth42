# Generated by Django 3.0.8 on 2020-07-23 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0007_dish_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='cost',
            new_name='price',
        ),
        migrations.AddField(
            model_name='shop',
            name='average_dish_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Средняя стоимость блюда'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/dish', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/shop', verbose_name='Фоторгафия заведения'),
        ),
    ]
