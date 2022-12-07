from django.db import models


class User(models.Model):
    STATE_CHOICES = [
        ('start', 1),
        ('main', 2),
        ('service', 3),
        ('master', 4),
        ('date', 5),
        ('registration', 6),
        ('consent', 7),
        ('name', 8),
        ('lk', 9)
    ]

    user_id = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, default='start', max_length=64)
    chosen_service = models.CharField(max_length=120, null=True)
    chosen_master = models.CharField(max_length=120, null=True)
    chosen_date = models.DateTimeField(null=True)
    full_name = models.CharField(max_length=120, null=True)
    phone_number = models.CharField(max_length=12, null=True)


class Menu(models.Model):
    state = models.CharField(choices=User.STATE_CHOICES, max_length=64)
    buttons = models.JSONField()
