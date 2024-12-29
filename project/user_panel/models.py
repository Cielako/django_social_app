from django.db import models
from users.models import CustomUser

# gettext_lazy is used widelly in multi language sites
from django.utils.translation import gettext_lazy as _

# Create your models here.

GENDER_CHOICES = {
    (0,_('male')),
    (1,_('female')),
    (2,_('not specified'))
}

ORIENTATION_CHOICES = {
    (0,_('heterosexual')),
    (1,_('homosexual')),
    (2,_('bisexual')),
    (3,_('asexual')),
}

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) # Delete profile when user is deleted
    first_name = models.CharField(max_length=30, blank=True)
    is_banned = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #location = models.
    about = models.CharField(max_length=256, blank=True, null=True)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    height = models.PositiveIntegerField()
    orientation = models.IntegerField(choices=ORIENTATION_CHOICES, default=0)
    #education = models.IntegerField(choices=ORIENTATION_CHOICES, default=0)
    #intrests
    #languages
    #looking_for