from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser

from ..managers import CustomUserManager


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(_("email address"), unique=True, null=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    is_student = models.BooleanField('student status', default=False)
    is_moderator = models.BooleanField('moderator status', default=False)

    objects = CustomUserManager()


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={'is_student': True},
        related_name='user'
    )
    parent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_student': False},
        related_name='parent'
    )
    chats = models.ManyToManyField('Chat')
    blocked_list = models.ManyToManyField(User)
    need = models.ManyToManyField('Topic', related_name='needed_by')
    offer = models.ManyToManyField('Topic', related_name='offered_by')
