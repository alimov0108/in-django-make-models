from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=258)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rasmcha = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.content} {self.date}"
