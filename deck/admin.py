from django.contrib import admin
from .models import Deck, Subject, Card

# Register your models here.

admin.site.register(Deck)
admin.site.register(Subject)
admin.site.register(Card)
