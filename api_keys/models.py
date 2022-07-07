from django.db import models

# Create your models here.


class APIKeys(models.Model):
    key = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
