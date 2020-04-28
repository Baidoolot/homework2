from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    book = models.FileField(upload_to='books/')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    post = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self): 
        return f'{self.post.title}, {self.body}'

