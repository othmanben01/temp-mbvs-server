from django.db import models
# Create your models here.
from users.models import User
from events.models import Event
from profiles.models import Profile
from roles.models import Role

class Subscription(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name='subscriptions')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=False, related_name='subscriptions')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, related_name='subscriptions')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=False, related_name='subscriptions', null=True)

    class Meta:
        unique_together = ('user', 'event', 'profile')
        ordering = ['created']

    # def __str__(self):
    #     return f'{self.name}'
