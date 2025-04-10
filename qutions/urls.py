from django.urls import path
from .views import UserCreateView, QuestionListView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='create-user'),
    path('questions/', QuestionListView.as_view(), name='get-questions'),
]
