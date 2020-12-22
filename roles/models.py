from django.db import models
# Create your models here.


class Role(models.Model):
    group = models.CharField(max_length=100, unique=True, blank=False, null=True)

    USERNAME_FIELD = 'group'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.group}'

    def save(self, *args, **kwargs):
        self.group = self.group.strip().lower()
        return super(Role, self).save(*args, **kwargs)