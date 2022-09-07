from django.db import models
class Contact(models.Model):
    email=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.email