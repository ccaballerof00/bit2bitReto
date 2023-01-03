from django.db import models
from django.contrib.postgres.fields import ArrayField

class Question (models.Model):
    Question_Id = models.AutoField(primary_key=True, db_index=True)
    Author = models.CharField(max_length=30, null=False)
    Title = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=2000, null=False)
    CreationDate = models.DateTimeField()
    Answers = ArrayField(models.CharField(max_length=15,null=True, default=[]))

    def str(self):
        return self.Question_Id

class Answer (models.Model):
    Answer_Id = models.AutoField(primary_key=True, db_index=True)
    Author = models.CharField(max_length=30, null=False)
    Description = models.CharField(max_length=2000, null=False)
    CreationDate = models.DateTimeField()

    def str(self):
        return self.Answer_Id