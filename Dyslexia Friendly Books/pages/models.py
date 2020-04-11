from django.db import models
from django import forms

PREFERENCES = [
    ('Text to Speech', 'Text to Speech'),
    ('Syllables', 'Syllables'),
    ('Synonyms', 'Synonyms'),
    ('Visual Editor', 'Visual Editor'),
    ]

class Book(models.Model):
    book_num = models.IntegerField(primary_key=True)
    book_title = models.CharField(max_length=100)
    book_author_fname = models.CharField(max_length=50, blank = True)
    book_author_lname = models.CharField(max_length=100, blank = True)
    book_cover_photo = models.ImageField(upload_to= 'book_covers', default='no-image-png.png')  

    def __str__(self):
        return self.book_title

    def get_book_name(number):
        books = Book.objects.all()
        for book in books:
            if book.book_num == number:
                return book.book_title


class Feedback(models.Model):
    userName = models.CharField(max_length=120)
    email = models.EmailField()
    firstPreference = forms.CharField(label='First Preference', widget=forms.Select(choices=PREFERENCES))
    secondPreference = forms.CharField(label='Second Preference', widget=forms.Select(choices=PREFERENCES))
    thirdPreference = forms.CharField(label='Third Preference', widget=forms.Select(choices=PREFERENCES))
    fourthPreference = forms.CharField(label='Fourth Preference', widget=forms.Select(choices=PREFERENCES))
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.userName

