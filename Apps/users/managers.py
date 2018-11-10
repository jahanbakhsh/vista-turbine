from django.contrib.auth.models import BaseUserManager
from django.db import models


class VODUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        """
        Creates and saves a User
        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, first_name, last_name):
        user = self.create_user(username=username, email=email, password=password, first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserQuerySet(models.QuerySet):
    def manager_and_queryset_method(self):
        pass


UserManager = VODUserManager.from_queryset(UserQuerySet)
