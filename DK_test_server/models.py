from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)


class Question(models.Model):
    question_text1 = models.CharField(max_length=100)
    question_text2 = models.CharField(max_length=100)
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date_publised")


class DateTraning(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, )
    date = models.DateTimeField()
    tranings_id = models.PositiveSmallIntegerField(primary_key=True)
    #push_ups = models.PositiveSmallIntegerField(default=0)
    #sit_ups = models.PositiveSmallIntegerField(default=0)
    #jumping = models.PositiveSmallIntegerField(default=0)
    #entrance = models.PositiveSmallIntegerField(default=0)
    #press = models.PositiveSmallIntegerField(default=0)
    #weight = models.PositiveSmallIntegerField(default=0)
    #weight_category = models.PositiveSmallIntegerField(default=0)
    #bars = models.PositiveSmallIntegerField(default=0)
    #stadium = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.id

class Pull(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    pull1 = models.PositiveSmallIntegerField(default=0)
    pull2 = models.PositiveSmallIntegerField(default=0)


class Push(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    push1 = models.PositiveSmallIntegerField(default=0)
    push2 = models.PositiveSmallIntegerField(default=0)


class Sit(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    sit1 = models.PositiveSmallIntegerField(default=0)
    sit2 = models.PositiveSmallIntegerField(default=0)


class Jumping(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    jumping1 = models.PositiveSmallIntegerField(default=0)
    jumping2 = models.PositiveSmallIntegerField(default=0)


class Entrance(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    entrance1 = models.PositiveSmallIntegerField(default=0)
    entrance2 = models.PositiveSmallIntegerField(default=0)


class Press(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    press1 = models.PositiveSmallIntegerField(default=0)
    press2 = models.PositiveSmallIntegerField(default=0)


class Weight(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    weight1 = models.PositiveSmallIntegerField(default=0)
    weight2 = models.PositiveSmallIntegerField(default=0)


class Weightcategory(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    weightcategory1 = models.PositiveSmallIntegerField(default=0)
    weightcategory2 = models.PositiveSmallIntegerField(default=0)


class Bars(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    bars1 = models.PositiveSmallIntegerField(default=0)
    bars2 = models.PositiveSmallIntegerField(default=0)


class Stadium(models.Model):
    id = models.OneToOneField(DateTraning, on_delete=models.CASCADE, primary_key=True)
    stadium1 = models.PositiveSmallIntegerField(default=0)
    stadium2 = models.PositiveSmallIntegerField(default=0)


# Create your models here.