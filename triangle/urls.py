from django.urls import path

from . import views

app_name = 'triangle'
urlpatterns = [
    path('', views.calculate_triangle, name='triangle')
]
