from django.db import models

# Create your models here.


class BookInfo(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    pub_date = models.DateField()

    def __str__(self):
        return '{} - {} -{}'.format(self.author, self.title, self.pub_date)