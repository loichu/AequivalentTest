from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(AbstractUser):
    phone = PhoneNumberField("phone number")
    count_checkAddr = models.IntegerField("count checkAddr requests")
    count_checkId = models.IntegerField("count checkID requests")
    count_auth = models.IntegerField("count checkID requests")
