from django.urls import path

from . import views
app_name = 'dashboard'

urlpatterns = [
    path('', views.display_badges, name='display_badges'),
]