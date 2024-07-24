from django.db import models

class Author(models.Model):
    firstname = models.CharField(max_length = 150)
    lastname = models.CharField(max_length = 200)
    email = models.CharField(max_length = 150)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Category(models.Model):
    cat_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.cat_name

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    likes = models.IntegerField(default = 0)
    author = models.ForeignKey("myblogs.Author", on_delete = models.PROTECT)
    date = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField("myblogs.Category")
    def __str__(self):
        return f"{self.title} ({self.likes})"

class Comment(models.Model):
    comment = models.CharField(max_length = 200)
    comment = models.ForeignKey("myblogs.Blog", on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
