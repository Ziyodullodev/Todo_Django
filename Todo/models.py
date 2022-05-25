from django.db import models

# Create your models here.


class TodoModels(models.Model):
    title = models.CharField(max_length=255)
    # desc = models.TextField()
    complate = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title