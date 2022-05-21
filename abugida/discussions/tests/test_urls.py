from ast import arg
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from discussions import views


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)
    
    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, views.about)

    def test_discussion_url_is_resolved(self):
        url = reverse('discussion')
        self.assertEqual(resolve(url).func, views.discussion)
    def test_rooms_url_is_resolved(self):
        url = reverse('rooms')
        self.assertEqual(resolve(url).func, views.rooms)
    def test_room_url_is_resolved(self):
        url = reverse('room', args=['pk'])
        self.assertEqual(resolve(url).func, views.room)
    
    def test_create_room_url_is_resolved(self):
        url = reverse('create-room')
        self.assertEqual(resolve(url).func, views.createRoom)

    def test_update_room_url_is_resolved(self):
        url = reverse('update-room', args=['pk'])
        self.assertEqual(resolve(url).func, views.updateRoom)
    
    def test_delete_room_url_is_resolved(self):
        url = reverse('delete-room', args=['pk'])
        self.assertEqual(resolve(url).func, views.deleteRoom)
    
    def test_create_question_url_is_resolved(self):
        url = reverse('create-question', args=['pk'])
        self.assertEqual(resolve(url).func, views.createQuestion)

    def test_update_question_url_is_resolved(self):
        url = reverse('update-question', args=['pk'])
        self.assertEqual(resolve(url).func, views.updateQuestion)
    
    def test_delete_question_url_is_resolved(self):
        url = reverse('delete-question', args=['pk'])
        self.assertEqual(resolve(url).func, views.deleteQuestion)
    
    def test_create_answer_url_is_resolved(self):
        url = reverse('create-answer', args=['pk'])
        self.assertEqual(resolve(url).func, views.createAnswer)

    def test_update_answer_url_is_resolved(self):
        url = reverse('update-answer', args=['pk'])
        self.assertEqual(resolve(url).func, views.updateAnswer)

    def test_delete_answer_url_is_resolved(self):
        url = reverse('delete-answer', args=['pk'])
        self.assertEqual(resolve(url).func, views.deleteAnswer)