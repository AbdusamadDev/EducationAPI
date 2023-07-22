from .models import Quiz, Category, Question, Answer, TestResult
from django.contrib import admin

admin.site.register(Quiz)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestResult)
