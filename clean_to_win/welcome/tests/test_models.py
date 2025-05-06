from datetime import datetime
from django.test import TestCase

from ..models import Feedback

class FeedbackModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all tests methods
        date_str = "2024-10-10 00:19:27.321587+0300"
        date_format = "%Y-%m-%d %H:%M:%S.%f%z"
        parsed_datetime = datetime.strptime(date_str, date_format)
        Feedback.objects.create(username='Big Bob', avatar_path='', short_msg='Feels very good',
                                text='OMG!!! love sorting trash!!!', created_at=parsed_datetime)

    def test_username_label(self):
        feedback = Feedback.objects.get(id=1)
        username = feedback._meta.get_field('username').verbose_name
        self.assertEqual(username, 'Никнейм пользователя')

    def test_avatar_path_label(self):
        feedback = Feedback.objects.get(id=1)
        avatar_path = feedback._meta.get_field('avatar_path').verbose_name
        self.assertEqual(avatar_path, 'Путь к аватарке')

    def test_short_msg_label(self):
        feedback = Feedback.objects.get(id=1)
        short_msg = feedback._meta.get_field('short_msg').verbose_name
        self.assertEqual(short_msg, 'Заголовок')

    def test_text_label(self):
        feedback = Feedback.objects.get(id=1)
        text = feedback._meta.get_field('text').verbose_name
        self.assertEqual(text, 'Текст отзыва')

    def test_text_label(self):
        feedback = Feedback.objects.get(id=1)
        created_at = feedback._meta.get_field('created_at').verbose_name
        self.assertEqual(created_at, 'Дата создания')

    def test_feedback_verbose_names(self):
        self.assertEqual(str(Feedback._meta.verbose_name), "Отзыв")
        self.assertEqual(str(Feedback._meta.verbose_name_plural), "Отзывы")

    def test_username_max_length(self):
        feedback = Feedback.objects.get(id=1)
        max_length = feedback._meta.get_field('username').max_length
        self.assertEqual(max_length, 100)

    def test_avatar_path_max_length(self):
        feedback = Feedback.objects.get(id=1)
        max_length = feedback._meta.get_field('avatar_path').max_length
        self.assertEqual(max_length, 255)

    def test_short_msg_max_length(self):
        feedback = Feedback.objects.get(id=1)
        max_length = feedback._meta.get_field('short_msg').max_length
        self.assertEqual(max_length, 40)

    def test_str_method_feedback(self):
        feedback = Feedback.objects.get(id=1)
        expected_object_name = f"{feedback.username} - {feedback.created_at.strftime('%Y-%m-%d %H:%M')}"
        self.assertEqual(expected_object_name, str(feedback))




from ..models import GalleryImages

class GalleryImagesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all tests methods
        date_str = "2024-10-10 00:19:27.321587+0300"
        date_format = "%Y-%m-%d %H:%M:%S.%f%z"
        parsed_datetime = datetime.strptime(date_str, date_format)
        GalleryImages.objects.create(name='composition_1', image='/welcome/images/composition_1.jpeg',
                                     description='Галлерея фото 1', upload_time=parsed_datetime)

    def test_name_max_length(self):
        gallery_image = GalleryImages.objects.get(id=1)
        max_length = gallery_image._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_image_max_length(self):
        gallery_image = GalleryImages.objects.get(id=1)
        max_length = gallery_image._meta.get_field('image').max_length
        self.assertEqual(max_length, 255)

    def test_str_method_feedback(self):
        gallery_image = GalleryImages.objects.get(id=1)
        expected_object_name = f"{gallery_image.name}"
        self.assertEqual(expected_object_name, str(gallery_image))
