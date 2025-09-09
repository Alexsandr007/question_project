import pytest
import uuid
from rest_framework.test import APIClient
from question_api.models import Question, Answer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def question():
    return Question.objects.create(
        text='Test Question Text'
    )

@pytest.fixture
def answer(question):
    return Answer.objects.create(
        question=question,
        user_id=uuid.uuid4(),
        text='Test Answer Text'
    )

@pytest.fixture
def question_data():
    return {
        'text': 'Test Question Text'
    }

@pytest.fixture
def answer_data():
    return {
        'user_id': str(uuid.uuid4()),
        'text': 'Test Answer Text'
    }