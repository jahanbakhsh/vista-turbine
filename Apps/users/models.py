from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import (UserManager)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=100, verbose_name=_('username'))
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True, verbose_name=_('Email'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # Manager
    objects = UserManager()

    # Meta & unicode
    def __str__(self):
        return self.username

    # Functions
    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None

        return super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        if not self.first_name or not self.last_name:
            return self.username

        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        if not self.first_name:
            return self.username

        return self.first_name

    # Admin required field
    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserStory(models.Model):
    user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,related_name="UserStory_created_by")
    updated_by = models.ForeignKey(User,related_name="UserStory_updated_by")