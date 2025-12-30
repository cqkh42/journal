from django.forms import ModelForm

from entries.models import Entry

class AuthorForm(ModelForm):
    class Meta:
        model = Entry
        fields = ["date", "text", "rating", "emoji"]