from django.urls import path
from .views import QuizListCreateAPIView, QuizRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('quizzes/', QuizListCreateAPIView.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizRetrieveUpdateDestroyAPIView.as_view(), name='quiz-detail'),
]
