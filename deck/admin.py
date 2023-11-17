from django.contrib import admin
from .models import deck, subject, card

# Register your models here.

admin.site.register(deck)
admin.site.register(subject)
admin.site.register(card)
