from django.db import models
# Create your models here.


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    is_shared = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        self.screen_name = self.screen_name.strip().lower()
        return super(Profile, self).save(*args, **kwargs)