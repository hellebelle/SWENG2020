
from django import template
from django.template.defaultfilters import stringfilter
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FeedbackForm

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


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'pages/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'pages/feedback.html', {'form': form})


def Book_view(request):
	books = Book.objects.all()
	args = {
		'books': books
	}
	return render(request, "pages/home.html", args)

def editor_view(request,  book_num):
	name = Book.get_book_name(book_num)
	bookText = strip_headers(load_etext(book_num)).strip()
	filteredText = removeStopWords(bookText)
	
	stopWords = request.session.get('stopWords')
	if stopWords is None:
		stopWords = True
		request.session['stopWords'] = stopWords

	args = {
		'content': [bookText], 'content2': [filteredText], 'name': name, 'stopWords' : stopWords
	}

	return render(request, "pages/editor.html", args)
	
def stopWordsToggle(request):
	print("RunToggle")
	stopWords = request.session.get('stopWords')
	stopWords = not stopWords
	request.session['stopWords'] = stopWords
	print(stopWords)

	return render(request, "pages/editor.html", {'stopWords' : stopWords})

def decison_view(request, book_num):
    args = {
        'bookNumber': book_num
    }
    return render(request, "pages/decision.html", args)

def feedback_view(request):
    return render(request, "pages/feedback.html")

def regular_view(request,  book_num):
	name = Book.get_book_name(book_num)
	bookText = strip_headers(load_etext(book_num)).strip()
	filteredText = removeStopWords(bookText)

	args = {
		'content': [bookText], 'content2': [filteredText], 'name': name
	}

	return render(request, "pages/regularText.html", args)

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

    filteredText = " ".join(filteredText)
    return filteredText

#returns the type of syllable, 
#returns "Error" if the text contains no vowels and is therefore not a syllable   
def getSyllableType(syllable):

    syllable = syllable.lower()
    lastIndex = len(syllable) - 1

    vowels = "aeiouy"
    syll = False
    count = 0

    for i in range(0, lastIndex + 1):

        if syllable[i] in vowels:
            syll = True
            count += 1

    if not syll:
        return "Error"

    if syllable[lastIndex] == 'e':

        if syllable[lastIndex - 1] == 'l':
            return "-le"
        if count >= 2 and not syllable[lastIndex - 1] in vowels: # At least two vowels (the last being 'e') with the second last letter being a consonant
            return "Magic E"

    if syllable[lastIndex] in vowels:
        return "Open"

    if syllable[lastIndex] == 'r':
        if syllable[lastIndex - 1] in vowels:
            return "R Controlled"

    for i in range(0, lastIndex):

        if syllable[i] in vowels:
            if syllable[i+1] in vowels:
                return "Vowel Team"

    return "Closed"
