from django.urls import path
from bookapi import views

from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'bookapi'

urlpatterns = [

    path('books/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('new_book', views.CreateBook.as_view()),
    
]

# You can choose, how to get/post data (JSON, HTML)
urlpatterns = format_suffix_patterns(urlpatterns)
