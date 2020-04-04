from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    url =models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    def get_abslute_url(self):
        return reverse('notepad:home', kwargs={"id": self.id})
    def get_update_url(self):
        return reverse('notepad:update', kwargs={"id": self.id})
    def get_delete_url(self):
        return reverse('notepad:delete', kwargs={"id": self.id})
