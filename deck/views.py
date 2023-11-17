from django.shortcuts import render, redirect
from .forms import DeckForm

# Create your views here.


def deck_list(request):
    return render(request, 'deck_list.html')

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