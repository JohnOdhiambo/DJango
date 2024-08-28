from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #Delete together with the user
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads')
    url = models.SlugField(unique=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message