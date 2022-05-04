from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.apps import apps


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where students have a username as unique
    identifier while other types of user have email.
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a generic User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a standard User with the given email and password.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)

    def create_student(self, username, password, **extra_fields):
        """
        Create and save a student User with the given username and password.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault("is_student", True)
        extra_fields.setdefault("is_moderator", False)

        if extra_fields.get('is_student') is not True:
            raise ValueError(_('Student must have is_student=True.'))
        if extra_fields.get('is_moderator') is True:
            raise ValueError(_('Student must have is_moderator=False.'))
        if not username:
            raise ValueError(_('The username must be set'))
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
