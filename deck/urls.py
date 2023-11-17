from django.urls import path
from . import views

urlpatterns = [
    path('decks', views.deck_list, name='home'),
    path('decks/add', views.new_deck, name='new-deck')
]