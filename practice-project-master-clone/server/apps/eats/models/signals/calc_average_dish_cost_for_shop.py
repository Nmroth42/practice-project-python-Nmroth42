from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.eats.models import Dish


@receiver([post_save, post_delete], sender=Dish)
def calc_average_dish_cost(sender, instance, **kwargs):
    instance.shop.average_dish_cost = Dish.objects.calc_average_dish_cost(
        instance.shop.id)
    instance.shop.save()
