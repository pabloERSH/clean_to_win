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

class Gallery(TemplateView):
    template_name = 'welcome/gallery.html'
    extra_context = {'menu': menu}
