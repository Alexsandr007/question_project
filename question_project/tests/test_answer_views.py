import pytest
from django.urls import reverse
from rest_framework import status
from question_api.models import Answer, Question


@pytest.mark.django_db
class TestAnswerCreateView:

    def test_create_answer_valid_data(self, api_client, question, answer_data):
        url = reverse('answers-create', kwargs={'question_id': question.pk})
        response = api_client.post(url, answer_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert Answer.objects.count() == 1
        answer = Answer.objects.first()
        assert answer.text == answer_data['text']
        assert str(answer.user_id) == answer_data['user_id']
        assert answer.question == question

    def test_create_answer_invalid_data(self, api_client, question):
        url = reverse('answers-create', kwargs={'question_id': question.pk})
        invalid_data = {'text': ''}  # Пустой текст
        response = api_client.post(url, invalid_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_answer_question_not_exists(self, api_client, answer_data):
        url = reverse('answers-create', kwargs={'question_id': 999})
        response = api_client.post(url, answer_data)

        assert response.status_code == status.HTTP_404_NOT_FOUND