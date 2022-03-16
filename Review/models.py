from django.db import models

# Create your models here.
class Reviews(models.Model):
    review_title = models.CharField(max_length=255)
    customer_review = models.CharField(max_length=255)