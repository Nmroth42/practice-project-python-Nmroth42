# Generated by Django 3.0.8 on 2020-07-22 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Название заведения')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Фоторгафия заведения')),
                ('work_start', models.TimeField(verbose_name='Начало рабочего дня')),
                ('work_end', models.TimeField(verbose_name='Конец рабочего дня')),
                ('addres', models.CharField(max_length=55, verbose_name='Адрес заведения')),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shops', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Заведение',
                'verbose_name_plural': 'Заведение',
            },
        ),
    ]