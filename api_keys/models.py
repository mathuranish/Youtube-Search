from django.db import models

# Create your models here.


class APIKeys(modelsModel):
    key = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
