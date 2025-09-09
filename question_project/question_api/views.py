from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
import logging
logger = logging.getLogger(__name__)

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer

class QuestionRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question_id = self.kwargs.get('question_id')
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise NotFound("Question not found")
        serializer.save(question=question)

class AnswerRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer