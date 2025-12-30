from django.views.generic import detail
from entries.views import index, EntryCreate, EntryDetail, EntryList

from django.urls import include, path
urlpatterns = [
    path("", index),
    path("entries/", EntryList.as_view(), name="list"),
    path("entries/create/", EntryCreate.as_view(), name="create"),
    path("entries/<int:pk>/", EntryDetail.as_view(), name="detail"),
]
