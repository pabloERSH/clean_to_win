from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class MainPage(TemplateView):
    template_name = 'telegram_app/main_page.html'
