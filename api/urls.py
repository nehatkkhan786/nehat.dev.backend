from django.urls import path
from .views import *


urlpatterns = [
    path('sendmessage/', ConactEmailView.as_view(),),
    path('getAllBlogs/', BlogView.as_view()),
    path('getblog/<int:pk>/', BlogDetailView.as_view()),
]