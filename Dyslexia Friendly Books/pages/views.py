from nltk.corpus import wordnet
from nltk.tokenize import SyllableTokenizer
import nltk
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .gutenbergtest import *
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata
from django import template
from django.template.defaultfilters import stringfilter
from django.http import JsonResponse
#	If google_speech is not installed please remove next line
from google_speech import Speech

register = template.Library()

def Book_view(request):
	books = Book.objects.all()
	args = {
		'books': books
	}
	return render(request, "pages/home.html", args)

def editor_view(request, book_num):
	name = Book.get_book_name(book_num)
	bookText = getBookTextByNumber(book_num, False)
	filteredText = removeStopWords(bookText)

	args = {
		'content': [bookText], 'content2': [filteredText], 'name': name
	}

	return render(request, "pages/editor.html", args)


#Returns a list of Syllables for the given word
def getSyllables(request, text):

	textSyllables = getTextSyllables(text)
	
	return JsonResponse(textSyllables, safe=False)

#returns list of synoynms for a word, 
#returns empty list if:
#                   string contains only digits
#                   string contains multiple words
#                   no synoynms available
def getSynoynms(request, text):
    synonyms = []
    #if string contains digits only
    if text.isdecimal():
        return synonyms
    else:
        #removing digits from string
        word = ''.join(filter(lambda x: x.isalpha(), text))
        #finding synoynms
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
        #removing duplicates
        returnLi = list(set(synonyms))
        #removing searched word
        if word in returnLi:
            returnLi.remove(word)
        return JsonResponse(returnLi, safe=False)

#Synthesizes speech from the given text
def getTextToSpeech(request, text):
    lang = "en"
    speech = Speech(text, lang)
    speech.play()

	
