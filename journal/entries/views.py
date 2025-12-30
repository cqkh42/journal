from datetime import date


from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
import pandas as pd

from entries.models import Entry

# Create your views here.
def index(request):
    today = date.today().strftime("%Y-%m-%d")
    days = pd.date_range(start="2025-12-01", end=min("2026-12-31", today), inclusive="both")
    days = {
        day: Entry.objects.filter(date=day).first()
        for day in days
    }
    return render(request, 'entries/index.html', context={"days":days})

class EntryCreate(CreateView):
    model = Entry
    fields = ["date", "text", "rating", "emoji"]

class EntryDetail(DetailView):
    model = Entry
    context_object_name = "entry"

class EntryList(ListView):
    model = Entry
    context_object_name = "entries"