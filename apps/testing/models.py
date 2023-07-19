from django.db import models
from apps.users.models import User
from apps.common.models import BaseModel


class TestResultModel(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    result = models.IntegerField()
    subject_id = models.ForeignKey(to="Subject", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Subject: %s --- User: %s --- Result: %s" % (self.subject_id, self.user_id, self.result)

class Subject(BaseModel):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject

class Question(BaseModel):
    text = models.CharField(max_length=450)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Variation(BaseModel):
    text = models.CharField(max_length=80)
    is_correct = models.BooleanField()
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
