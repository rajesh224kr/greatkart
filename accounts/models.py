from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
         def create_user(self,first_name,last_name,username,email, password = None):
                  if not email:
                           raise ValueError('User must have an email address')
                  if not username:
                           raise ValueError('User must have an username')
                  user = self.model(
                           email = self.normalize_email(email),
                           username= username,
                           first_name= first_name,
                           last_name = last_name,

                  )
                  user.set_password(password)
                  user.save(using = self._db)
                  return user

         def create_superuser(self,first_name,last_name,username,email, password = None):
                  user = self.create_user(
                           email = self.normalize_email(email),
                           username= username,
                           first_name= first_name,
                           last_name = last_name,
                  )
                  user.is_admin = True
                  user.is_active = True
                  user.is_superuser = True 
                  # user.is_staff = True
                  
                  user.save(using = self._db)
                  return user


class Account(AbstractBaseUser):
         first_name = models.CharField(max_length=50)
         last_name = models.CharField(max_length=50)
         username = models.CharField(max_length=50, unique=True)
         email = models.EmailField(max_length=50, unique=True)
         phone_number = models.IntegerField(blank=True,null=True)

         #requried field
         date_joined = models.DateField(auto_now_add=True)         
         last_login = models.DateField(auto_now_add=True) 
         is_admin = models.BooleanField(default=True)        
         # is_staff = models.BooleanField(default=False)        
         is_active = models.BooleanField(default=False)        
         is_superadmin = models.BooleanField(default=False)        

         USERNAME_FIELD = 'email'
         REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
         
         # calling Manager
         objects = MyAccountManager()
         
         class Meta:
                  ordering = ['-id']
         
         def __str__(self):
                  return self.email
         
         # if the user is admin , he is permission to change the user
         # permission
         def has_perm(self, perm, obj = None):
                  return self.is_admin
         # it should alway true
         def has_module_perms(self,add_label):
                  return True







