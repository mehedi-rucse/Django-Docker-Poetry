from django.urls import path
from public import views

urlpatterns = [
    path('', views.get, name = 'index'),
]