from google_speech import Speech

def TTS(text):
    lang = "en"
    speech = Speech(text, lang)
    speech.play()

