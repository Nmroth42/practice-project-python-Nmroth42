from django.db import models


class Ingredient(models.Model):
    name = models.CharField(verbose_name='Название', max_length=33)
    calories = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ['-id']

    def __str__(self):
        return self.name
