# Generated by Django 3.0.8 on 2020-07-22 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0003_auto_20200722_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фоторгафия заведения'),
        ),
    ]
