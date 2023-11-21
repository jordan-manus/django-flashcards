from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, CardForm
from .models import Deck, Card
from django.views import generic
import random
# from accounts.models import CustomUser

# Create your views here.

@login_required
def deck_list(request):
    # decks = Deck.objects.filter(CustomUser=request.user)
    decks = Deck.objects.filter(user=request.user)
    # creates error when editing/deleting deck objects: 'WSGIRequest' object has no attribute 'username'
    return render(
                request,
                'deck_list.html',
                {'decks': decks})


def new_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeckForm()
    return render(
        request,
        'new_deck.html',
        {'form': form}
    )


def new_card(request, pk):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deck-details', pk=pk)
    else:
        form = CardForm()
    return render(
        request,
        'new_card.html',
        {'form': form}
        )


# class DeckDetailsView(generic.DetailView):
#     model = Deck
#     template_name = 'deck_details.html'
    # does card_details need to be added here?

def card_details(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = Card.objects.filter(deck=deck)
    return render(request, 'deck_details.html', {'cards': cards, 'deck': deck})
    

def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)

    if request.method == 'GET':
        context = {'form': DeckForm(instance=deck), 'pk': pk}
        return render(request, 'new_deck.html', context)

    elif request.method == 'POST':
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'new_deck.html', {'form': form})
        

def delete_deck(request, pk):
    delete_deck = get_object_or_404(Deck, pk=pk)
    delete_deck.delete()
    return redirect('home')


def edit_card(request, pk, card_pk):
    card = get_object_or_404(Card, pk=card_pk)

    if request.method == 'GET':
        context = {'form': CardForm(instance=card), 'pk': card_pk}
        return render(request, 'new_card.html', context)

    elif request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('deck-details', pk=pk)
        else:
            return render(request, 'new_card.html', {'form': form})
        

def delete_card(request, pk, card_pk):
    delete_card = get_object_or_404(Card, pk=card_pk)
    delete_card.delete()
    return redirect('deck-details', pk=pk)
