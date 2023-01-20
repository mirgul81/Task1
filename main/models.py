from django.db import models


class News(models.Model):
    title = models.CharField(max_length=60)
    info = models.TextField()

    def __str__(self):
        return self.title

class Students(models.Model):
        name = models.CharField(max_length=50)
        surname = models.CharField(max_length=50)
        age = models.PositiveIntegerField()
        faculty = models.CharField(max_length=50)

        def __str__(self):
            return self.name


class Abouts(models.Model):
    title = models.CharField(max_length=60)
    info = models.TextField()

    def __str__(self):
        return self.title


