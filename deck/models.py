from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Deck(models.Model):
    title = models.CharField("Title", max_length=150, blank=True, null=True)
    subject = models.CharField("Subject", max_length=150, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    question = models.TextField(max_length=1000, help_text="Enter a question")
    answer = models.TextField(max_length=1000, help_text="Enter an answer")

    def __str__(self) -> str:
        return self.name


# class Subject(models.Model):
#     name = models.CharField(max_length=150, help_text='Pick a subject')

#     def __str__(self):
#         return self.name



