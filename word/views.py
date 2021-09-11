from django.shortcuts import render
from .models import Word

# Create your views here.
def index(request):
    word = Word.objects.random()
    return render(request, 'word/index.html', {'word': word})