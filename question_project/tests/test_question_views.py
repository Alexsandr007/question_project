import pytest
from django.urls import reverse
from rest_framework import status
from question_api.models import Question


@pytest.mark.django_db
class TestQuestionListCreateView:

    def test_list_questions(self, api_client, question):
        url = reverse('questions-list-create')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['text'] == question.text

    def test_create_question_valid_data(self, api_client, question_data):
        url = reverse('questions-list-create')
        response = api_client.post(url, question_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert Question.objects.count() == 1
        assert Question.objects.first().text == question_data['text']

    def test_create_question_invalid_data(self, api_client):
        url = reverse('questions-list-create')
        invalid_data = {'text': ''}  # Пустой текст
        response = api_client.post(url, invalid_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_questions_ordered_by_created_at(self, api_client):
        # Создаем вопросы
        question1 = Question.objects.create(text='Question 1')
        question2 = Question.objects.create(text='Question 2')

        url = reverse('questions-list-create')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['id'] == question2.id