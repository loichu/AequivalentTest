from django.test import TestCase

from .models import Student #, User
from django.contrib.auth import get_user_model


class UserTest(TestCase):

    def standard_user_checks(self, user):
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_moderator)

    def test_create_parent(self):
        User = get_user_model()
        user = User.objects.create_user(email='john.doe@e2e.ch', password='foo')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'john.doe@e2e.ch')
        self.standard_user_checks(user)
        self.assertFalse(user.is_student)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_student(self):
        User = get_user_model()
        user = User.objects.create_student(username='john.doe', password='foo')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'john.doe')
        self.standard_user_checks(user)
        self.assertTrue(user.is_student)
        try:
            self.assertIsNone(user.email)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_student()
        with self.assertRaises(TypeError):
            User.objects.create_student(username='')
        with self.assertRaises(ValueError):
            User.objects.create_student(username='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
