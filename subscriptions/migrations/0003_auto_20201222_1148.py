# Generated by Django 3.1.4 on 2020-12-22 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roles', '0001_initial'),
        ('events', '0002_auto_20201222_1025'),
        ('profiles', '0001_initial'),
        ('subscriptions', '0002_auto_20201222_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions_event', to='events.event'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions_profile', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='role', to='roles.role'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
