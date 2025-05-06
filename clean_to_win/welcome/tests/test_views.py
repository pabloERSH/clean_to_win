from datetime import datetime

from django.test import TestCase

#test of Index view

from ..models import GalleryImages
from ..models import Feedback
from ..views import menu
from django.urls import reverse

class IndexListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        date_str = "2024-10-10 00:19:27.321587+0300"
        date_format = "%Y-%m-%d %H:%M:%S.%f%z"
        parsed_datetime = datetime.strptime(date_str, date_format)
        GalleryImages.objects.create(name='composition_1', image='/welcome/images/composition_1.jpeg',
                                     description='Галлерея фото 1', upload_time=parsed_datetime)
        GalleryImages.objects.create(name='composition_2', image='/welcome/images/composition_2.jpeg',
                                              description='Галлерея фото 2', upload_time=parsed_datetime)
        GalleryImages.objects.create(name='composition_3', image='/welcome/images/composition_3.jpeg',
                                              description='Галлерея фото 3', upload_time=parsed_datetime)
        Feedback.objects.create(username='Big Bob', avatar_path='path/to/avatar1', short_msg='Feels very good',
                                text='OMG!!! love sorting trash!!!', created_at=parsed_datetime)
        Feedback.objects.create(username='Small Tom', avatar_path='path/to/avatar1', short_msg='I find new friends',
                                text='Great feeling!!! Now Im helping our ecology!!!', created_at=parsed_datetime)

    def test_page_accessible(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'welcome/index.html')

    def test_context_data(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('menu', response.context)
        self.assertIn('feedbacks', response.context)
        self.assertEqual(response.context['menu'], menu)
        self.assertEqual(len(response.context['images']), 3)
        self.assertEqual(len(response.context['feedbacks']), 2)


#test of About view

class AboutTemplateViewTest(TestCase):

    def test_page_accessible(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/about.html')

    def test_context_data(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('menu', response.context)
        self.assertEqual(response.context['menu'], menu)


#test of Feedback view

class FeedBackListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        date_str = "2024-10-10 00:19:27.321587+0300"
        date_format = "%Y-%m-%d %H:%M:%S.%f%z"
        parsed_datetime = datetime.strptime(date_str, date_format)

        for i in range(7):
            Feedback.objects.create(username=f'user{i}', avatar_path=f'path/to/avatar{i}',
                                    short_msg='Feels very good',
                                    text='OMG!!! love sorting trash!!!', created_at=parsed_datetime)

    def test_page_accessible(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/feedback.html')

    def test_context_data(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('menu', response.context)
        self.assertIn('feedbacks', response.context)
        self.assertEqual(response.context['menu'], menu)
        self.assertEqual(len(response.context['feedbacks']), 7)

#test of Gallery view

class GalleryListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        date_str = "2024-10-10 00:19:27.321587+0300"
        date_format = "%Y-%m-%d %H:%M:%S.%f%z"
        parsed_datetime = datetime.strptime(date_str, date_format)

        for i in range(15):
            GalleryImages.objects.create(name=f'composition_{i}', image=f'/welcome/images/composition_{i}.jpeg',
                                         description=f'Галлерея фото {i}', upload_time=parsed_datetime)


    def test_page_accessible(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/gallery.html')

    def test_context_data(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('menu', response.context)
        self.assertIn('compositions', response.context)
        self.assertIn('gallery', response.context)
        self.assertEqual(response.context['menu'], menu)
        self.assertEqual(len(response.context['compositions']), 3)
