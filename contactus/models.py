from django.db import models

# Create your models here.


class contact(models.Model):
    Name = models.CharField(max_length=200)
    Mail = models.EmailField(max_length=200)
    Sub = models.CharField(max_length=200)
    Msg = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name
