from django.db import models


class Review(models.Model):
    fullname = models.CharField(max_length=150)
    message = models.CharField(max_length=350)
    photo = models.ImageField(upload_to='static/images/reviewphoto')

    def __str__(self):
        return self.fullname


    @staticmethod
    def get_all_reviews():
        return Review.objects.all()
