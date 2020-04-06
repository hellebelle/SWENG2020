from django.urls import path
from pages.views import *

urlpatterns = [
    path('', Book_view, name = "book"),
    path('getSyllables/<str:text>', getSyllables, name="getSyllables"),
    path('getSynoynms/<str:text>', getSynoynms, name="getSynoynms"),
    path('getTextToSpeech/<str:text>', getTextToSpeech, name="getTextToSpeech"),
    path('<int:book_num>/', editor_view, name="editor"),

]
