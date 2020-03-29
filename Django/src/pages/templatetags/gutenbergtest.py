from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
import nltk
from nltk.tokenize import SyllableTokenizer
from nltk.corpus import wordnet
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

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
            count+=1

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

def createBookPages(text, charCount):
    
    pageText = ([text[i:i+charCount] for i in range(0, len(text), charCount)]) 

    return pageText

def getBookPage2(text, charCount, pageNumber):

    startChar = ((pageNumber - 1) * charCount)
    
    pageText = text[startChar:startChar+charCount]

    return pageText

def getBookPage(text, wordCount, pageNumber):

    startWord = ((pageNumber - 1) * wordCount)

    data = text.split()
    #data = nltk.word_tokenize(text)
    data = data[startWord:startWord+wordCount]

    pageText = " "
    pageText = pageText.join(data)

    # for ele in data:  
    #     pageText += ele   

    return pageText


def testBookPage(text, charCount):
    
    print([text[i:i+charCount] for i in range(0, len(text), charCount)]) 

def findBookByAuthor(bookAuthor):
    bookName = get_etexts('author', bookAuthor)  
    print(bookName)
    return

def getBookTextByNumber(bookID, strip):

    bookText = load_etext(bookID)

    if strip:
        bookText = strip_headers(bookText).strip()
        
    return bookText

#returns list of synoynms for a word, 
#returns empty list if:
#                   string contains only digits
#                   string contains multiple words
#                   no synoynms available
def getSynoynms(s):
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
        return returnLi
    
@register.filter(name='getTextSyllables')
@stringfilter
def getTextSyllables(text):
    print(text)
    print("hello")
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
    
    print(textSyllables)
    return textSyllables

# bookText = getBookTextByNumber(2701, True)
# pageText = getBookPage(bookText, 3000, 1)
# print(getTextSyllables(pageText))

#findBookByAuthor('Melville, Hermann')

# print(getSyllableType("test"))
# print(getSyllableType("be"))
# print(getSyllableType("came"))
# print(getSyllableType("far"))
# print(getSyllableType("team"))
# print(getSyllableType("cle"))
# print(getSyllableType("BRB"))

# bookText = getBookTextByNumber(2701, True)

# #print(getBookPage(text, 3000, 1))

# pageText = getBookPage(bookText, 3000, 1)

# print("Created Page 1")

# SSP = SyllableTokenizer()

# tokenised_sentences = nltk.sent_tokenize(pageText)
# for sentence in tokenised_sentences:
#     tokenised_words = nltk.word_tokenize(sentence)


#     tagged_words = nltk.pos_tag(tokenised_words)
#     for word in tokenised_words:
#         tokenised_syllables = SSP.tokenize(word)
#         #print(tokenised_syllables)
    




