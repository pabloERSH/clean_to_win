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
    queryset = GalleryImages.objects.order_by('?')[:3]
    template_name = 'welcome/index.html'
    context_object_name = 'images'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['feedbacks'] = Feedback.objects.order_by('?')[:2]
        return context

class About(TemplateView):
    template_name = 'welcome/about.html'
    extra_context = {'menu': menu}


class FeedBack(ListView):
    queryset = Feedback.objects.order_by('?')[:7]
    template_name = 'welcome/feedback.html'
    context_object_name = 'feedbacks'
    extra_context = {'menu': menu}


class Gallery(ListView):
    model = GalleryImages
    template_name = 'welcome/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['compositions'] = GalleryImages.objects.filter(name__icontains='composition').order_by('?')[:3]
        context['gallery'] = GalleryImages.objects.filter(name__icontains='Gallery').order_by('?')[:12]
        return context
