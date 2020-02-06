from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = "<html><body>Dyslexic Friendly Books</body></html>"
    return HttpResponse(html)
