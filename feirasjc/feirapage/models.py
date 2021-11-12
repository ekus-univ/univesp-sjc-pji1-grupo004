from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField('Título', max_length=200)
    author = models.CharField('Autor', max_length=100)
    text = models.TextField('Depoimento')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
