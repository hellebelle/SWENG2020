from django.db import models

class Book(models.Model):
    book_num = models.IntegerField(primary_key=True)
    book_title = models.CharField(max_length=100)
    book_author_fname = models.CharField(max_length=50, blank = True)
    book_author_lname = models.CharField(max_length=100, blank = True)
    book_cover_photo = models.ImageField(upload_to= 'book_covers', default='no-image-png.png')  

    def __str__(self):
        return self.book_title

    def get_book_num(self):
        bookNumber  = self.book_num

        return bookNumber