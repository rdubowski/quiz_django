from django.urls import path, include
from .views import Quiz, RandomQuestion
app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>', RandomQuestion.as_view(), name='random'),
]
