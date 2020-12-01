from django.db import models
from django.db.models import Avg, Sum

from apps.eats.models import Ingredient, Shop


class DishManager(models.Manager):
    def calc_average_dish_cost(self, shop_id):
        return self.filter(shop__id=shop_id).aggregate(
            Avg('price'))['price__avg'] or 0


class Dish(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='dishes',
        verbose_name='Заведение'
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='dishes',
        verbose_name='Ингредиенты',
        blank=True
    )

    name = models.CharField(
        verbose_name='Название',
        max_length=55,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='images/dish',
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    @property
    def calories_sum(self):
        return self.ingredients.all().aggregate(
            calories_sum=Sum('calories'))['calories_sum']

    objects = DishManager()

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['-id']

    def __str__(self):
        return self.name
