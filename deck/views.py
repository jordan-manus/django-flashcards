from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, CardForm
from .models import Deck, Card
import random

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

@login_required
def new_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('home')
    else:
        form = DeckForm()
    return render(
        request,
        'new_deck.html',
        {'form': form}
    )


@login_required
def new_card(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.deck = deck
            card.save()
            return redirect('deck-details', pk=pk)
    else:
        form = CardForm()
    return render(
        request,
        'new_card.html',
        {'form': form}
        )


@login_required
def card_details(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = Card.objects.filter(deck=deck)
    cards = cards.order_by('?')
    return render(request, 'deck_details.html', {'cards': cards, 'deck': deck})
    

@login_required
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
        
@login_required
def delete_deck(request, pk):
    delete_deck = get_object_or_404(Deck, pk=pk)
    delete_deck.delete()
    return redirect('home')

@login_required
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
        
@login_required
def delete_card(request, pk, card_pk):
    delete_card = get_object_or_404(Card, pk=card_pk)
    delete_card.delete()
    return redirect('deck-details', pk=pk)
