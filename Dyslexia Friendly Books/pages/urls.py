from django.urls import path
from pages.views import *

urlpatterns = [
    path('', Book_view, name = "book"),
    path('getSyllables/<str:text>', getSyllables, name="getSyllables"),
    path('getSynoynms/<str:text>', getSynoynms, name="getSynoynms"),
    path('getTextToSpeech/<str:text>', getTextToSpeech, name="getTextToSpeech"),
		path('stopWordsToggle/', stopWordsToggle, name="stopWordsToggle"),
    path('<int:book_num>/', decison_view, name="decision"),
    path('<int:book_num>/editor', editor_view, name="editor"),
    path('<int:book_num>/regular', regular_view, name="regular"),
    path('feedback', feedback_form, name="feedback"),
]

