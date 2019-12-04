from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.

class userProfileTestCase(APITestCase):
    profile_list_url = reverse('all-profiles')
 
    def setUp(self):
        #make a post request to create a new user
        self.user = self.client.post('/auth/users/', data={'username':'johndoe', 'password':'secret123#'})
        # obtain a json web token for the newly created user
        response = self.client.post('/auth/jwt/create/', data={'username':'johndoe', 'password':'secret123#'})
        self.token = response.data['access']
        self.authenticate()
    
    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    def test_authenticated_user_can_retrieve_profile_list(self):
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_retrieve_profile_list(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

    def test_retrieve_authenticated_user_profile(self):
        response=self.client.get(reverse('profile',kwargs={'pk':1}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_add_user_profile(self):
        payload={
            'description': 'I love football',
            'location': 'Accra',
            'is_creator': 'true',
        }
        
        response = self.client.put(reverse('profile', kwargs={'pk': 1}), data= payload)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)