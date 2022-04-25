
from django.db import models
from sampleapp.manager import CustomUserManager
from django.contrib.auth.models import PermissionsMixin ,AbstractBaseUser
from django.conf import settings
from django.utils import timezone
# Create your models here.
#name--200
#email--256
#file--
#contact--character
class Book(models.Model):
    bookname=models.CharField(max_length=255,null=True)
    book_file=models.FileField(blank=True,null=False)
    book_upload_date=models.DateTimeField(auto_now=True,null=False)
class B2CUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(('email address'),unique=True)
    name=models.CharField(max_length=255,null=True)
    contact=models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','contact']
    objects=CustomUserManager()
    def __str__(self):
        return '(%s,%s)' %(self.email,self.name)
    
    
## mtwo model commands
# python--queries
# queries ExecutionLoader
# ##python manage.py makemigrations ---
# we are creating the complex queries  from python to quries  
# python manage.py migrate...execution of queries 
    # python manage.py makemigrations ---for entire project 
    # python manage.py migrate
      
    # python manage.py makemigrations app_name1
    # python manage.py migrate app_name1
