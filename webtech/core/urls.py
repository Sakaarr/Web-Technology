from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.forms, name='forms'),
    path('success/', views.success_view, name='success'),
]
