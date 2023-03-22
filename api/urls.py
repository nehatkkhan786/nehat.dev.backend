from django.urls import path
from .views import *


urlpatterns = [
    path('sendmessage/', ConactEmailView.as_view(),),
]