from google_speech import Speech

print("Please enter text to synthesize:")
text = input()
lang = "en"
speech = Speech(text, lang)
speech.play()