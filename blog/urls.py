from django.urls import path
from . import views
from .views import BlogList, BlogDetailView

urlpatterns = [
    path("blogs/", BlogList.as_view(), name="blog-list-create"),         
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
]
