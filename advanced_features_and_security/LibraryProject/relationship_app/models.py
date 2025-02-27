from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def _str_(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    USER_ROLES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='Member')

    def _str_(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def _str_(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True,blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/',null=True,blank=True)

    def __str__(self):
        return self.username
    
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,date_of_birth=None,profile_photo=None,**extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,date_of_birth=date_of+birth,profile_photo=profile_photo,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password=None,date_of_birth=None,profile_photo=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superpower',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username,email,password,date_of_birth,profile_photo,**extra_fields)
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True,blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/',null=True,blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username