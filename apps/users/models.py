from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import BaseModel

from .managers import UserManager


class User(AbstractUser, BaseModel):
    full_name = models.CharField(_("Full Name"), max_length=255, null=True, blank=True)
    username = None
    phone = models.CharField(_("Phone"), max_length=14, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    faculty = models.CharField(_("Faculty"), max_length=255)
    course = models.CharField(_("Course"), max_length=255)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # type: ignore

    def __str__(self):
        if self.email:
            return self.email

    @property
    def tokens(self):
        token = RefreshToken.for_user(self)
        return {"access": str(token.access_token), "refresh": str(token)}

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
