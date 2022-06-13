from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)


class Question(models.Model):
    question_text1 = models.CharField(max_length=100)
    question_text2 = models.CharField(max_length=100)
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date_publised")


# Create your models here.