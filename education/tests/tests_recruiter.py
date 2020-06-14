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


class EducationRecruiterTestCase(TestCase):

    def setUp(self):

        # Creamos un usuario reclutador para comprobar que no tiene acceso
        user = User(
            email='testing_login@cosasdedevs.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login',
            is_recruiter=True
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

    
    def test_create_education_recruiter(self):

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(result['detail'], 'You do not have permission to perform this action.')

    
    def test_update_education(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        test_education_update = {
            'date_ini': '2010-09-02T19:41:21Z',
            'date_end': '2012-09-02T19:41:21Z',
            'title': 'DAA',
        }

        response = client.put(
            '/education/1/', 
            test_education_update,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(result['detail'], 'You do not have permission to perform this action.')

    
    def test_delete_education(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        response = client.delete(
            '/education/1/', 
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(result['detail'], 'You do not have permission to perform this action.')


    def test_get_education(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        response = client.get('/education/')

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(result['detail'], 'You do not have permission to perform this action.')