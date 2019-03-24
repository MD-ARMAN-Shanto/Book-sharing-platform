from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings
# Create your models here.


class BookList(models.Model):
    book_title = models.CharField(max_length=30)
    book_author = models.CharField(max_length=30)
    book_edition = models.CharField(max_length=10)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    user_phn = models.CharField(max_length=15)
    book_image = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title + " - " + self.book_author+ " - " + str(self.user)



    #def __unicode__(self):
        #return str(self.user.username)



