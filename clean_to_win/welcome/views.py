from django.views.generic import TemplateView, ListView
from .models import GalleryImages
from django.views.generic import TemplateView, ListView

from .models import Feedback

menu = {
    'О нашем проекте': '/about',
    'Отзывы': '/feedback',
    'Галерея': '/gallery',
    'Главная': '../'
}


class Index(ListView):
    queryset = Feedback.objects.order_by('?')[:2]
    context_object_name = 'feedbacks'
    template_name = 'welcome/index.html'
    extra_context = {'menu': menu}

class About(TemplateView):
    template_name = 'welcome/about.html'
    extra_context = {'menu': menu}


class FeedBack(ListView):
    #model = Feedback
    queryset = Feedback.objects.order_by('?')[:7]
    template_name = 'welcome/feedback.html'
    context_object_name = 'feedbacks'
    extra_context = {'menu': menu}


class Gallery(ListView):
    model = GalleryImages
    template_name = 'welcome/gallery.html'
    context_object_name = 'images'
    extra_context = {'menu': menu}

    def get_queryset(self):
        # Получаем 15 случайных объектов
        return GalleryImages.objects.order_by("?")[:15]





