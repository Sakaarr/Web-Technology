from django.db import models

# Create your models here.

class MyFormModel(models.Model):
    email = models.EmailField()
    example_select = models.IntegerField()
    example_textarea = models.TextField()

    def __str__(self):
        return self.email
