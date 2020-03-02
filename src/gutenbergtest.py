from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata

import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def findBookByAuthor(bookAuthor):
    bookName = get_etexts('author', bookAuthor)  
    print(bookName)
    return

def getBookTextByNumber(bookID, strip):

    bookText = load_etext(bookID)

    if strip:
        bookText = strip_headers(bookText).strip()
        
    return bookText


text = getBookTextByNumber(2701, True)
tokenised_sentences = nltk.sent_tokenize(text)
for sentence in tokenised_sentences:
    tokenised_words = nltk.word_tokenize(sentence)


    tagged_words = nltk.pos_tag(tokenised_words)
    
print(tagged_words)
#findBookByAuthor('Melville, Hermann')

