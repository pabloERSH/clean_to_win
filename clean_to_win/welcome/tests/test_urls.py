from django.test import TestCase, Client
from django.urls import reverse


class WelcomeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/about.html')

    def test_feedback_view(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/feedback.html')

    def test_gallery_view(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/gallery.html')
