from django.urls import path

from . import views
app_name = 'books'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit_comment, name='edit'),
    path('<int:pk>/delete/', views.delete_comment, name='delete'),
    path('my_books/', views.view_shelves, name='view_shelves'),
]