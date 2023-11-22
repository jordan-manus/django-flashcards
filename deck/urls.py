from django.urls import path
from . import views


urlpatterns = [
    path('', views.deck_list, name='home'),
    path('add', views.new_deck, name='new-deck'),
    # path('decks/<int:pk>', views.DeckDetailsView.as_view(), name='deck-details'),
    path('<int:pk>', views.card_details, name='deck-details'),
    path('<int:pk>/edit', views.edit_deck, name='edit-deck'),
    path('<int:pk>/delete', views.delete_deck, name='delete-deck'),
    path('<int:pk>/new_card', views.new_card, name='new-card'),
    path('<int:pk>/card<int:card_pk>/edit', views.edit_card, name='edit-card'),
    path('<int:pk>/card<int:card_pk>/delete', views.delete_card, name='delete-card'),
]