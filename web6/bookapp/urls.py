from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_cover, name='book_cover'),
]
