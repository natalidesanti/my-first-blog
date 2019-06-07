from django.db import models
from django.utils import timezone

# class object, Post is the choosen model, models.Model means that it is a Django model
class Post(models.Model): 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #defines a text with a limited number of characters
    text = models.TextField() #defines a text with unlimited chars
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
