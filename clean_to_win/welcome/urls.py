from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('feedback/', views.FeedBack.as_view(), name='feedback'),
    path('gallery/', views.Gallery.as_view(), name='gallery')
]