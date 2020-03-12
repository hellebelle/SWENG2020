from django.http import HttpResponse
from django.shortcuts import render

from pages.gutenbergtest import getBookTextByNumber

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def editor_view(request):
    return render(request, "editor.html", {'content':[getBookTextByNumber(2701, False)]})
