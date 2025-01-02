from django.db import models

# Create your models here.

class LostItem(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_lost = models.DateField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name