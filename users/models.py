from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


# Create your models here.
class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    business_name = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(blank=True, null=True, max_length=20)
    gender = models.CharField(blank=True, null=True, max_length=50)
    image = models.CharField(blank=True, null=True, max_length=1024)
    about = models.TextField(blank=True, null=True)
    terms_and_condition = models.BooleanField(default=False)
    

    def __str__(self):
        return "{} @ {}".format(self.get_full_name(), self.email)

    def get_full_name(self):
        return self.first_name +' '+ self.last_name