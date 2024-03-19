from django.urls import path
from .views import view_chat

urlpatterns = [
    path('', view_chat, name='view-chat'),
]