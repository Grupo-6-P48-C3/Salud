from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not email:
            raise ValueError('Users must have an username')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
        email,password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField('Email', max_length = 100, unique=True)
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 60)
    telephone = models.BigIntegerField('Telephone',null=True)
 
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'email'