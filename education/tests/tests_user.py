# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from education.models import Education
from users.models import User


class EducationTestCase(TestCase):

    def setUp(self):

        # Creamos un usuario y generamos el acceso a la api para hacer pruebas de forma general
        user = User(
            email='testing_login@cosasdedevs.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()

        client = APIClient()
        response = client.post(
                '/users/login/', {
                'email': 'testing_login@cosasdedevs.com',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access_token = result['access_token']
        self.user = user


    def test_create_education(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        test_education = {
            'date_ini': '2010-09-01T19:41:21Z',
            'date_end': '2012-09-01T19:41:21Z',
            'title': 'Desarrollo de Aplicaciones informáticas',
        }

        response = client.post(
            '/education/', 
            test_education,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('pk', result)
        self.assertIn('date_ini', result)
        self.assertIn('date_end', result)
        self.assertIn('title', result)

        if 'pk' in result:
            del result['pk']

        self.assertEqual(result, test_education)


    def test_update_education(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        # Creamos un objeto en la base de datos para trabajar con datos
        edu = Education.objects.create(
            date_ini='2010-09-01T19:41:21Z',
            date_end='2012-09-01T19:41:21Z',
            title='DAM',
            user=self.user
        )

        test_education_update = {
            'date_ini': '2010-09-02T19:41:21Z',
            'date_end': '2012-09-02T19:41:21Z',
            'title': 'DAA',
        }

        response = client.put(
            f'/education/{edu.pk}/', 
            test_education_update,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if 'pk' in result:
            del result['pk']

        self.assertEqual(result, test_education_update)

    
    def test_delete_education(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        # Creamos un objeto en la base de datos para trabajar con datos
        edu = Education.objects.create(
            date_ini='2010-09-01T19:41:21Z',
            date_end='2012-09-01T19:41:21Z',
            title='DAM',
            user=self.user
        )

        response = client.delete(
            f'/education/{edu.pk}/', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        edu_exists = Education.objects.filter(pk=edu.pk)
        self.assertFalse(edu_exists)


    def test_get_education(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        Education.objects.create(
            date_ini='2010-09-01T19:41:21Z',
            date_end='2012-09-01T19:41:21Z',
            title='DAM',
            user=self.user
        )

        Education.objects.create(
            date_ini='2008-09-01T19:41:21Z',
            date_end='2010-09-01T19:41:21Z',
            title='Bachiller',
            user=self.user
        )

        response = client.get('/education/')
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result['count'], 2)

        for edu in result['results']:
            self.assertIn('pk', edu)
            self.assertIn('date_ini', edu)
            self.assertIn('date_end', edu)
            self.assertIn('title', edu)
            break