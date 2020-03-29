from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .gutenbergtest import *


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def editor_view(request , book_num):
    # if request.is_ajax() and request.method == "POST":
    #     textSelected = request.POST['text']
	
	name = Book.get_book_name(book_num)

	if request.method == 'POST':
		print("Run2")
		if request.POST.get('type') and request.POST.get('type') == "syll":
			
			print("Run3")
		
			textSelected = request.POST.get('sel')
			
			print(textSelected)
			
			syllables = getTextSyllables(textSelected) 
			
			print(syllables)
			
	args = {
		'content':[getBookTextByNumber(book_num, False)],'name' : name
	}
	
	return render(request, "editor.html", args)

def Book_view(request):
	print("Run1")
	books = Book.objects.all()
	args = {
		'books' : books
	}
	return render(request, "home.html", args)
  

	