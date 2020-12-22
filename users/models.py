from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser):
    username = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return f'{self.username}'

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.first_name = self.first_name.strip().lower()
        self.last_name = self.last_name.strip().lower()
        return super(User, self).save(*args, **kwargs)
