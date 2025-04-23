from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email :
            raise ValueError("Email is must provided!")
        email = self.normalize_email(email) #Normalize the email address by lowercasing the domain part of it.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    fullName =models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']

    def __str__(self):
        return self.email