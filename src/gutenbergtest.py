from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

text = strip_headers(load_etext(2701)).strip()
tokenised_sentences = nltk.sent_tokenize(text)
for sentence in tokenised_sentences:
    tokenised_words = nltk.word_tokenize(sentence)


    tagged_words = nltk.pos_tag(tokenised_words)
    
print(tagged_words)