from .gutenbergtest import getBookTextByNumber, getTextSyllables, getSynoynms, getSyllableType

def Syllables(request):
    text = request.GET['sel']
    syllables = getTextSyllables(text)
    return syllables

def Synonyns(request):
    text = request.GET['sel']
    synonyms = getSynoynms(text)
    return synonyms