from django.contrib import admin
from .models import Book, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('firstPreference', 'secondPreference', 'thirdPreference', 'fourthPreference', 'userName', 'date', 'happy',)

    class Meta:
        model = Feedback


admin.site.register(Book)
admin.site.register(Feedback, FeedbackAdmin)
