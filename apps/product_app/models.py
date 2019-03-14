from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PHONE_REGEX= re.compile(r'^[2-9]\d{2}-\d{3}-\d{4}$')
INVENTORY_REGEX= re.compile(r'^[1-100]+$')
import bcrypt

class Validation(models.Manager):
    def user_login_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) <  2:
            errors['first_name'] = "First name needs to be at least 2 characters."
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name needs to be at least 2 characters."
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email entered."
        if post_data['email'] == User.objects.filter(email=post_data['email']):
            errors['email'] = "Email already registered. Please use login."
        if not PHONE_REGEX.match(post_data['phone']):
            errors['phone'] = "Invalid phone entered. the pattern is 800-555-5555"
        if post_data['password1'] != post_data['password2']:
            errors['password1'] = "Passwords do not match."
        if len(post_data['password1']) < 8:
            errors['password1'] = "Password needs to be at least 8 characters."
        return errors

    def product_validator(self, post_data):
        errors = {}
        if len(post_data['product_name']) <  2:
            errors['product_name'] = "Product name needs to be at least 2 characters."
        if len(post_data['product_desc']) < 2:
            errors['product_desc'] = "Product description needs to be at least 2 characters."
        if len(post_data['product_gender']) < 1:
            errors['product_gender'] = "Please select gender"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    phone_no=models.CharField(max_length=255)
    password = models.CharField(max_length=64)
    create_at = models.DateTimeField(auto_now_add=True)
    objects = Validation()

class Address(models.Model):
    street_name = models.CharField(max_length=300)
    city_name = models.CharField(max_length=300)
    state_name = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    User = models.ForeignKey(User,related_name="address")
    create_at = models.DateTimeField(auto_now_add=True)

class Upper_category(models.Model):
    upper_name=models.CharField(max_length=100)

class Lower_category(models.Model):
    lower_name=models.CharField(max_length=100)
    Upper_category = models.ForeignKey(Upper_category,related_name="big_category")

class Product_Info(models.Model):
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=500)
    product_gender=models.CharField(max_length=10)
    product_price=models.CharField(max_length=20)
    product_inventory=models.CharField(max_length=20)
    product_path=models.CharField(max_length=200)
    Upper_category = models.ForeignKey(Upper_category,related_name="upper_category")
    Lower_category=models.ForeignKey(Lower_category,related_name="small_category")
    objects = Validation()
