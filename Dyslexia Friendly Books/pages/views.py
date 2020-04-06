
from django import template
from django.template.defaultfilters import stringfilter
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render

import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import SyllableTokenizer

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata

from google_speech import Speech

from .models import Book

register = template.Library()

def Book_view(request):
	books = Book.objects.all()
	args = {
		'books': books
	}
	return render(request, "pages/home.html", args)

def editor_view(request, book_num):
	name = Book.get_book_name(book_num)
	bookText = strip_headers(load_etext(book_num)).strip()
	filteredText = removeStopWords(bookText)

	args = {
		'content': [bookText], 'content2': [filteredText], 'name': name
	}

	return render(request, "pages/editor.html", args)

#Returns a list of Syllables for the given word
def getSyllables(request, text):
    textSyllables = []
    SSP = SyllableTokenizer()
    tokenised_sentences = nltk.sent_tokenize(text)
    for sentence in tokenised_sentences:
        tokenised_words = nltk.word_tokenize(sentence)
        #tagged_words = nltk.pos_tag(tokenised_words)
        for word in tokenised_words:
            tokenised_syllables = SSP.tokenize(word)
            #textSyllables = textSyllables.join(tokenised_syllables)
            textSyllables += tokenised_syllables
	
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

#returns text with stop words removed
def removeStopWords(text):
    stopWords = set(stopwords.words('english')) 
    tokenisedWords = nltk.word_tokenize(text)

    filteredText = [w for w in tokenisedWords if not w in stopWords] 
  
    filteredText = [] 
    
    for w in tokenisedWords: 
        if w not in stopWords: 
            filteredText.append(w) 

    return filteredText

