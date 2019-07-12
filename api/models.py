from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps django work with custom user model"""
    
    def create_user(self,email,name,password):
        """Creates new user"""

        if not email:
            raise ValueError('Users must have an email address')
        
        email =self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """Creates and saves new super user"""
        
        user = self.create_user(email,name,password)
        
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
        



class UserProfile(BaseUserManager, PermissionsMixin):
    """Respents user profile inside our system"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)


    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get full name of the user"""

        return self.name

    def get_short_name(self):
        """used to get short name of the user"""

        return self.name


    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email