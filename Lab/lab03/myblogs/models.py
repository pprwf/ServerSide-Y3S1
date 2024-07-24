from django.db import models
from datetime import date

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    tagline = models.TextField()
    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.CharField(max_length = 200)
    email = models.EmailField()
    def __str__(self):
        return self.user

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    headline = models.CharField(max_length = 255)
    body = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default = date.today)
    authors = models.ManyToManyField(Author)
    comments = models.IntegerField(default = 0)
    pingbacks = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 5)
    def __str__(self):
        return self.headline
