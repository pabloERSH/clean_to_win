from django.views.generic import TemplateView, ListView
from .models import GalleryImages


menu = {
    'О нашем проекте': '/about',
    'Отзывы': '/feedback',
    'Галерея': '/gallery',
    'Главная': '../'
}


class Index(TemplateView):
    template_name = 'welcome/index.html'
    extra_context = {'menu': menu}


class About(TemplateView):
    template_name = 'welcome/about.html'
    extra_context = {'menu': menu}


class FeedBack(TemplateView):
    template_name = 'welcome/feedback.html'
    extra_context = {'menu': menu}


class Gallery(ListView):
    model = GalleryImages
    template_name = 'welcome/gallery.html'
    context_object_name = 'images'
    extra_context = {'menu': menu}

    def get_queryset(self):
        # Получаем 15 случайных объектов
        return GalleryImages.objects.order_by("?")[:15]





