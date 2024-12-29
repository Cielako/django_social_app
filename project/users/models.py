from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
# gettext_lazy is used widelly in multi language sites
from django.utils.translation import gettext_lazy as _

# AbstractUser - standard user model 
# AbstraceBaseUser - user model that we creating from scratch


# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model that creates regular users and superusers.
    """
    
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError(_("The Username field must be set."))
        if not email:
            raise ValueError(_("The Email field must be set."))
        
        # Optionally convert the username to lowercase if required
        username = username.lower()  # Optional, based on your use case
        email = self.normalize_email(email)
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        if not password:
            raise ValueError(_("The Password field must be set for superusers."))

        return self.create_user(username, email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that requires a unique username and email.
    """
    username = models.CharField(_("username"), max_length=35, unique=True)
    email = models.EmailField(_("email address"), max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Fixed typo here
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)  # Let Django handle last_login
    
    # Linking the custom manager
    objects = CustomUserManager()
    
    # Fields used for authentication
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']  # When creating superuser, this field is required
    
    def __str__(self):
        return self.username
    
