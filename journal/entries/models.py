from django.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):

    date = models.DateField()
    text = models.TextField()
    rating = models.IntegerField()
    emoji = models.TextField()

    def get_absolute_url(self):
        return reverse("entries:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.date} {self.pk}"
