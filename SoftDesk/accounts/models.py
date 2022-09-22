from tabnanny import verbose
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.

class UserTheme(models.Model):
    THEME_CHOICES = (
        ('cyborg', 'cyborg'),
        ('cerulean', 'cerulean'),
        ('lux', 'lux'),
        ('lumen', 'lumen'),
        ('simplex', 'simplex'),
        ('morph', 'morph'),
        ('minty', 'minty'),
        ('slate', 'slate'),
        ('vapor', 'vapor'),
        ('zephyr', 'zephyr'),
    )    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(choices=THEME_CHOICES, default='cyborg', max_length=10)

    def __str__(self):
        return "theme: " + self.user.username
