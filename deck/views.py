from django.shortcuts import render, redirect
from .forms import DeckForm, CardForm
from .models import Deck
from django.views import generic

# Create your views here.


def deck_list(request):
    decks = Deck.objects.all()
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


class DeckDetailsView(generic.DetailView):
    model = Deck
    template_name = 'deck_details.html'
