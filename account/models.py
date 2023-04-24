from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email,password,phone,**kwargs):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        #user = self.model
        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)  ### hash of password
        user.save() ## saving user in bd
        return user



    def create_superuser(self, email, password, phone,**kwargs):
        if not email:
            raise ValueError('Email is required')
        kwargs['is_staff'] =True
        kwargs['is_superuser'] = True
        kwargs['is_active'] = True
        email = self.normalize_email(email)
        # user = self.model
        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    username = None  # removing username
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    bio = models.TextField()

    # managery zachem pereopredeliajutsya v django
    USERNAME_FIELD ='email'  # pointing on what fields use during login
    REQUIRED_FIELDS =['phone']


    objects = UserManager() # making new manager







