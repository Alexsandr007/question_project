import pytest
from django.urls import reverse
from rest_framework import status
from question_api.models import Question


@pytest.mark.django_db
class TestQuestionRetrieveDestroyView:

    def test_retrieve_question_exists(self, api_client, question):
        url = reverse('questions-detail', kwargs={'pk': question.pk})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['text'] == question.text

    def test_retrieve_question_not_exists(self, api_client):
        url = reverse('questions-detail', kwargs={'pk': 999})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_question_exists(self, api_client, question):
        url = reverse('questions-detail', kwargs={'pk': question.pk})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Question.objects.count() == 0

    def test_delete_question_not_exists(self, api_client):
        url = reverse('questions-detail', kwargs={'pk': 999})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND