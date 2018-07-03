from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=64,default='Title')
    content = models.TextField(null=True)


