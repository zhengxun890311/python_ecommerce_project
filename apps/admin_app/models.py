from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# Create your models here.
class Validation(models.Manager):
    def admin_register_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 3:
            errors['first_name'] = "First name needs to be at least 2 characters."
        if len(post_data['last_name']) < 3:
            errors['last_name'] = "Last name needs to be at least 2 characters."
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email entered."
        if post_data['email'] == Admin.objects.filter(admin_email=post_data['email']):
            errors['email'] = "Email already registered. Please use login."
        if post_data['password1'] != post_data['password2']:
            errors['password1'] = "Passwords do not match."
        if len(post_data['password1']) < 8:
            errors['password1'] = "Password needs to be at least 8 characters."
        return errors

class Admin(models.Model):
    admin_first_name = models.CharField(max_length=64)
    admin_last_name = models.CharField(max_length=64)
    admin_email=models.CharField(max_length=64)
    admin_password = models.CharField(max_length=64)
    admin_authority= models.CharField(max_length=10)
    admin_create_at = models.DateTimeField(auto_now_add=True)
    objects = Validation()