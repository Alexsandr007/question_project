import pytest
from django.urls import reverse
from rest_framework import status
from question_api.models import Answer


@pytest.mark.django_db
class TestAnswerRetrieveDestroyView:

    def test_retrieve_answer_exists(self, api_client, answer):
        """Test retrieving an existing answer"""
        url = reverse('answers-detail', kwargs={'pk': answer.pk})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['text'] == answer.text
        assert response.data['user_id'] == str(answer.user_id)

    def test_retrieve_answer_not_exists(self, api_client):
        url = reverse('answers-detail', kwargs={'pk': 999})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_answer_exists(self, api_client, answer):
        url = reverse('answers-detail', kwargs={'pk': answer.pk})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Answer.objects.count() == 0

    def test_delete_answer_not_exists(self, api_client):
        url = reverse('answers-detail', kwargs={'pk': 999})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND