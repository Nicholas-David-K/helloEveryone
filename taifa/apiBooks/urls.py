from django.urls import path
from . import views

urlpatterns = [
    path("ebooks/", views.EbookListCreateAPIView.as_view(), name="ebooks-list"),
    path("ebooks/<int:pk>/", views.EbookDetailAPIView.as_view(), name="ebooks-detail"),

    path('ebooks/<int:ebook_pk>/review/', 
         views.ReviewListCreateAPIView.as_view(), 
         name='ebook-review'),

    path('review/<int:pk>/', 
         views.ReviewDetailAPIView.as_view() , 
         name='reviews-detail'),
]
    