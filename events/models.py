from django.db import models
# Create your models here.


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        return super(Event, self).save(*args, **kwargs)