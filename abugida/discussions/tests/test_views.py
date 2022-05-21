from django.test import TestCase, Client
from django.urls import reverse
from discussions import models

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.about_url = reverse('about')
        self.course_url = reverse('course')
        self.discussion_url = reverse('discussion')
        self.rooms_url = reverse('rooms')


    def test_home_page_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'discussions/index.html')
    
    def test_about_page_GET(self):
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'discussions/about.html')

    def test_course_page_GET(self):
        response = self.client.get(self.course_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'discussions/about.html')

    def test_discussion_page_GET(self):
        response = self.client.get(self.discussion_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'discussions/discussions.html')

    def test_course_page_GET(self):
        response = self.client.get(self.discussion_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'discussions/discussions.html')

    def test_rooms_page_GET(self):
        response = self.client.get(self.rooms_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'discussions/rooms.html')



