from django.db import models

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)  # Store quiz score

class Question(models.Model):
    STATUS_CHOICES = [
        ("answered", "Answered"),
        ("skipped", "Skipped"),
        ("not answered", "Not Answered"),
    ]

    question_text = models.TextField()
    options = models.JSONField()  # Store options as JSON (e.g., ["A", "B", "C", "D"])
    correct_answer = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="not answered")  # Restrict choices

    def __str__(self):
        return self.question_text

