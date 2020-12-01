from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Владелец',
        related_name='shops',
    )

    name = models.CharField(
        max_length=55,
        verbose_name='Название заведения',
    )
    image = models.ImageField(
        upload_to='images/shop',
        verbose_name='Фоторгафия заведения',
        blank=True,
        null=True,
    )
    work_start = models.TimeField(
        verbose_name='Начало рабочего дня',
    )

    work_end = models.TimeField(
        verbose_name='Конец рабочего дня',
    )
    addres = models.CharField(
        max_length=55,
        verbose_name='Адрес заведения',
    )

    latitude = models.DecimalField(
        verbose_name='Широта',
        max_digits=10,
        decimal_places=5,
        default=0.0
    )
    longitude = models.DecimalField(
        verbose_name='Долгота',
        max_digits=10,
        decimal_places=5,
        default=0.0
    )

    average_dish_cost = models.DecimalField(
        verbose_name='Средняя стоимость блюда',
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'
        ordering = ['-id']
