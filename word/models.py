from random import randint
from django.db import models
from django.db.models import Count


class WordsManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

class Word(models.Model):
    objects = WordsManager()
    word = models.CharField(max_length=30)

    def __str__(self):
        return self.word