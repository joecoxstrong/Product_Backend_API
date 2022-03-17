from tkinter.tix import COLUMN
from django.db import models
# from sqlalchemy import ForeignKey
from products.models import Product

# Create your models here.
# class Reviews(models.Model):
#     review_title = models.CharField(max_length=255)
#     customer_review = models.CharField(max_length=255)

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    title = models.CharField(max_length=50, default=None)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)

def __str__(self) -> str:
        return self.title