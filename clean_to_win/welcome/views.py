from django.views.generic import TemplateView


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

class Gallery(TemplateView):
    template_name = 'welcome/gallery.html'
    extra_context = {'menu': menu}
