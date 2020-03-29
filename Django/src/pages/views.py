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


register = template.Library()


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


def editor_view(request, book_num):
    # if request.is_ajax() and request.method == "POST":
    #     textSelected = request.POST['text']

	name = Book.get_book_name(book_num)

	if request.method == 'POST':
		print("Run2")
		if request.POST.get('type') and request.POST.get('type') == "syll":

			print("Run3")

			textSelected = request.POST.get('sel')

			print(textSelected)

			# syllables = getTextSyllables(textSelected)

			# print(syllables)

	args = {
		'content': [getBookTextByNumber(book_num, False)], 'name': name
	}

	return render(request, "editor.html", args)


def Book_view(request):
	print("Run1")
	books = Book.objects.all()
	args = {
		'books': books
	}
	return render(request, "home.html", args)


def getTextSyllables(request, txt):
	print(txt)
	textSyllables = []
	SSP = SyllableTokenizer()
	tokenised_sentences = nltk.sent_tokenize(txt)
	for sentence in tokenised_sentences:
		tokenised_words = nltk.word_tokenize(sentence)
		#tagged_words = nltk.pos_tag(tokenised_words)
		for word in tokenised_words:
			tokenised_syllables = SSP.tokenize(word)
			# textSyllables = textSyllables.join(tokenised_syllables)
			textSyllables += tokenised_syllables
	print(textSyllables)
	
	return JsonResponse(textSyllables, safe=False)

#returns list of synoynms for a word, 
#returns empty list if:
#                   string contains only digits
#                   string contains multiple words
#                   no synoynms available
def getSynoynms(request, s):
    synonyms = []
    #if string contains digits only
    if s.isdecimal():
        return synonyms
    else:
        #removing digits from string
        word = ''.join(filter(lambda x: x.isalpha(), s))
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


	
