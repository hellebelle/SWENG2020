from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from pages.gutenbergtest import getBookTextByNumber

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def editor_view(request):
    return render(request, "editor.html", {'content':[getBookTextByNumber(11, False)]})

def Book_view(request):
  books = Book.objects.all()
  args = {
      'books' : books
  }
  return render(request, "home.html", args)