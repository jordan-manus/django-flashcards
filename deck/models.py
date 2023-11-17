from django.db import models

# Create your models here.


class Deck(models.Model):
    title = models.CharField("Title", max_length=150, blank=False)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField(max_length=150, help_text='Pick a subject')

    def __str__(self):
        return self.name


class Card(models.Model):
    question = models.TextField(max_length=1000, help_text="Enter a question")
    answer = models.TextField(max_length=1000, help_text="Enter an answer")

