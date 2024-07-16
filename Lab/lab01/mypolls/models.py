from django.db import models

class Question(models.Model):
    question = models.CharField(max_length = 200)
    date = models.DateTimeField("Date Published")
    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice
