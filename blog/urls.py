from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view()),
    path('<slug:slug>/', BlogDetailView.as_view()),
]