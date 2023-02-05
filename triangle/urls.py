from django.urls import path

from . import views

app_name = 'person'
urlpatterns = [
    path('triangle', views.calculate_triangle, name='triangle'),
    path('', views.create_person, name='create_person'),
    path('<int:pk>', views.edit_person, name='edit_person')
]
