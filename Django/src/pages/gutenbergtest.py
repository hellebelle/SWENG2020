from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata

import nltk
from nltk.tokenize import SyllableTokenizer
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

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


#findBookByAuthor('Melville, Hermann')

bookText = getBookTextByNumber(2701, True)

#print(getBookPage(text, 3000, 1))

pageText = getBookPage(bookText, 3000, 1)

print("Created Page 1")

SSP = SyllableTokenizer()


tokenised_sentences = nltk.sent_tokenize(pageText)
for sentence in tokenised_sentences:
    tokenised_words = nltk.word_tokenize(sentence)


    tagged_words = nltk.pos_tag(tokenised_words)
    for word in tokenised_words:
        tokenised_syllables = SSP.tokenize(word)
        #print(tokenised_syllables)
    





