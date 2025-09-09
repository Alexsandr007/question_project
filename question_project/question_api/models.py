from django.db import models
import uuid

class Question(models.Model):
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user_id = models.UUIDField()
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)