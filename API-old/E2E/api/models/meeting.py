from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Meeting(models.Model):
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    bidirectional = models.BooleanField()
    helper = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
    )


class Grade(models.Model):
    meeting = models.ForeignKey(
        'Meeting',
        null=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
    )
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )