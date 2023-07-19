from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have a email!")
        if not password:
            raise ValueError("User must have  password!")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if not password:
            raise ValueError("User must have  password!")
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
