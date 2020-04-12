from django.db import models
from django import forms

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
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
    Name = models.CharField(max_length=120)
    email = models.EmailField()
    firstPreference = forms.CharField(label='First Preference', widget=forms.Select(choices='TTS'))
    secondPreference = forms.CharField(label='Second Preference', widget=forms.Select(choices=FAVORITE_COLORS_CHOICES))
    thirdPreference = forms.CharField(label='Third Preference', widget=forms.Select(choices=FAVORITE_COLORS_CHOICES))
    fourthPreference = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    Improvements = models.TextField(blank=True)
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name

