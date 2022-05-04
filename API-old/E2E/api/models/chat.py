from django.db import models
from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Chat(models.Model):
    confirmed = models.BooleanField(default=False)
    requested_by = models.ForeignKey(
        'Student',
        on_delete=models.SET(get_sentinel_user),
        related_name="requests",
    )
    reported_by = models.ForeignKey(
        'Student',
        on_delete=models.SET(get_sentinel_user),
        related_name="reported_chats",
    )


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(
        'Student',
        on_delete=models.SET(get_sentinel_user),
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.SET(get_sentinel_user),
    )