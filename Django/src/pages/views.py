from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Book
from .gutenbergtest import getBookTextByNumber, getTextSyllables, getSynoynms, getSyllableType
from .googleTTS import TTS
from . import test


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def editor_view(request , book_num):
    name = Book.get_book_name(book_num)
    context = {
        'content': [getBookTextByNumber(11, False)],
        'name': name,
    }
    return render(request, "editor.html", context)

def Book_view(request):
  books = Book.objects.all()
  args = {
      'books' : books
  }
  return render(request, "home.html", args)

def Syllables(request):
    text = request.GET['sel']
    syllables = getTextSyllables(text)
    syllableTypes = []
    for s in syllables:
        syllableTypes.append(s)
    name = Book.get_book_name(11)
    context = {
        'content':[getBookTextByNumber(11, False)],
        'name': name,
        'Syllables': syllables,
        'SyllableTypes': syllableTypes,
    }
    return render(request, 'editor.html', context)

def Speak(request):
      text = request.GET['sel']
      TTS(text)
      return HttpResponseRedirect('Syllables/')

def Synonyms(request):
    text = request.GET['sel']
    synonyms = getSynoynms(text)
    name = Book.get_book_name(11)
    context = {
        'content': [getBookTextByNumber(11, False)],
        'name': name,
        'Synonyms': synonyms,
    }
    return render(request, 'editor.html', context)