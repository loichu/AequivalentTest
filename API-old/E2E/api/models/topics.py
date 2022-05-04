from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
