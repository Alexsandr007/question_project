from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.QuestionListCreateView.as_view(), name='questions-list-create'),
    path('questions/<int:pk>/', views.QuestionRetrieveDestroyView.as_view(), name='questions-detail'),
    path('questions/<int:question_id>/answers/', views.AnswerCreateView.as_view(), name='answers-create'),
    path('answers/<int:pk>/', views.AnswerRetrieveDestroyView.as_view(), name='answers-detail'),
]