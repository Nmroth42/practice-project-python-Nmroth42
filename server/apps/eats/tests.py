import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.eats.models import Shop, Dish


class EatsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.token = Token.objects.create(user=self.user)

        self.shop_data = {
            'owner_id': self.user.id,
            'name': 'shop',
            'image': None,
            'work_start': '00:13:00',
            'work_end': '12:34:00',
            'addres': 'г. Красноярск, ул. Академика Киренского, 26, корп. 1',
        }

        self.dish_data = {
            'name': 'dish',
            'image': None,
            'price': '23.00',
            'shop': None,
            'ingredients': []
        }


##################################################################
# Shop test
##################################################################

    def test_post_shop_action(self):
        """
        По POST-запросу на /api/eats возвращается 201, если пользователь авторизован
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.client.credentials()
        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_shop_action(self):
        """
        По GET-запросу на /api/eats возвращается 200.
        """
        response = self.client.get('/api/eats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_shop_action(self):
        """
        По PUT-запросу на /api/eats возвращается 200, если его
        выполняет владелец
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на изменение владельцем
        current_shop_id = Shop.objects.first().id
        self.shop_data['name']='updated'
        response = self.client.put('/api/eats/{}/'.format(current_shop_id), self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # проверка на изменение не владельцем
        other_owner = User.objects.create_user(username='other_owner', password='test')
        token = Token.objects.create(user=other_owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))
        response = self.client.put('/api/eats/{}/'.format(current_shop_id), self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_shop_action(self):
        """
        По PATCH-запросу на /api/eats возвращается 200, если его
        выполняет владелец
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на изменение владельцем
        current_shop_id = Shop.objects.first().id
        self.shop_data['name']='updated'
        response = self.client.patch('/api/eats/{}/'.format(current_shop_id), self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # проверка на изменение не владельцем
        other_owner = User.objects.create_user(username='other_owner', password='test')
        token = Token.objects.create(user=other_owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))

        response = self.client.patch('/api/eats/{}/'.format(current_shop_id), self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_shop_action(self):
        """
        По DELETE-запросу на /api/eats возвращается 200, если его
        выполняет владелец
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на удаление владельцем
        current_shop_id = Shop.objects.first().id
        response = self.client.delete('/api/eats/{}/'.format(current_shop_id), self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на удаление не владельцем
        current_shop_id = Shop.objects.first().id
        other_owner = User.objects.create_user(username='other_owner', password='test')
        token = Token.objects.create(user=other_owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))

        response = self.client.delete('/api/eats/{}/'.format(current_shop_id), self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#################################################################
# Dish test
#################################################################

    def test_post_dish_action(self):
        """
        По POST-запросу на /api/dishes возвращается 201, если его
        выполняет владелец.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        response = self.client.post('/api/eats/', self.shop_data, format='json')

        # проверка на добавление владельцем
        current_shop_id = Shop.objects.first().id
        self.dish_data['shop'] = current_shop_id
        response = self.client.post('/api/dishes/', self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка на добавление не владельцем
        other_owner = User.objects.create_user(username='other_owner', password='test')
        token = Token.objects.create(user=other_owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))

        response = self.client.post('/api/dishes/', self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_dish_action(self):
        """
        По GET-запросу на /api/dishes возвращается 200.
        """
        response = self.client.get('/api/dishes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_dish_action(self):
        """
        По PUT-запросу на /api/dishes возвращается 200, если его
        выполняет владелец
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        current_shop_id = Shop.objects.first().id
        self.dish_data['shop'] = current_shop_id
        response = self.client.post('/api/dishes/', self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на изменение владельцем
        current_dish_id = Dish.objects.first().id
        self.dish_data['name']='updated'
        response = self.client.put('/api/dishes/{}/'.format(current_dish_id), self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # проверка на изменение не владельцем
        other_owner = User.objects.create_user(username='other_owner', password='test')
        token = Token.objects.create(user=other_owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))
        response = self.client.put('/api/dishes/{}/'.format(current_dish_id), self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_dish_action(self):
        """
        По PATCH-запросу на /api/dishes возвращается 200, если его
        выполняет владелец
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        current_shop_id = Shop.objects.first().id
        self.dish_data['shop'] = current_shop_id
        response = self.client.post('/api/dishes/', self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на изменение владельцем
        current_dish_id = Dish.objects.first().id
        self.dish_data['name']='updated'
        response = self.client.patch('/api/dishes/{}/'.format(current_dish_id), self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # проверка на изменение не владельцем
        other_owner = User.objects.create_user(username='other_owner', password='test')
        token = Token.objects.create(user=other_owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))
        response = self.client.patch('/api/dishes/{}/'.format(current_dish_id), self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_dish_action(self):
        """
        По DELETE-запросу на /api/dishes возвращается 200, если его
        выполняет владелец
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        response = self.client.post('/api/eats/', self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        current_shop_id = Shop.objects.first().id
        self.dish_data['shop'] = current_shop_id
        response = self.client.post('/api/dishes/', self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на удаление владельцем
        current_dish_id = Dish.objects.first().id
        response = self.client.delete('/api/dishes/{}/'.format(current_dish_id), self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.post('/api/dishes/', self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка на удаление не владельцем
        current_dish_id = Dish.objects.first().id
        other_owner = User.objects.create_user(username='other_owner', password='test')
        token = Token.objects.create(user=other_owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))

        response = self.client.delete('/api/dishes/{}/'.format(current_dish_id), self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
