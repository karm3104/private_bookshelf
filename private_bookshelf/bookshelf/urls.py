from django.urls import path
from . import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('book-list/', views.BookshelfListView.as_view(), name="book_list"),
    path('book-detail/<int:pk>/', views.BookshelfDetailView.as_view(), name="book_detail"),
    path('book-create/', views.BookshelfCreateView.as_view(), name="book_create"),
    path('book-update/<int:pk>/', views.BookshelfUpdateView.as_view(), name="book_update"),
    path('book-delete/<int:pk>/', views.BookshelfDeleteView.as_view(), name="book_delete"),
]