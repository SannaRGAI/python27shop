from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string
from .utils import send_activation_code



class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email,password,phone,**kwargs):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        #user = self.model
        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)  ### hash of password
        user.create_activation_code()
        send_activation_code(user.email, user.activation_code)
        user.save(using=self._db) ## saving user in bd
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
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)



    # managery zachem pereopredeliajutsya v django
    USERNAME_FIELD ='email'  # pointing on what fields use during login
    REQUIRED_FIELDS =['phone']


    objects = UserManager() # making new manager
    def create_activation_code(self):
        code = get_random_string(length=8)
        self.activation_code = code
        self.save()







