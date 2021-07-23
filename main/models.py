from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    highlighted = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)



