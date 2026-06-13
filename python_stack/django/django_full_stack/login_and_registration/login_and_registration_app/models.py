from django.db import models
from datetime import date
import re 

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        first_name = postData.get('first_name', '').strip()
        last_name = postData.get('last_name', '').strip()
        email = postData.get('email', '').strip()
        password = postData.get('password', '').strip()
        confirm_pw = postData.get('confirm_pw', '').strip()
        birth_date = postData.get('birth_date')

        if not EMAIL_REGEX.match(email):
            errors['email'] = "Invalid email address!"

        if User.objects.filter(email__iexact=email).exists():
            errors['email'] = "An email should be unique"

        if birth_date:
            birth_date = date.fromisoformat(birth_date)
            if birth_date > date.today():
                errors['birth_date'] = "Birth date must be in the past."

            age = date.today().year - birth_date.year
            if (date.today().month, date.today().day) < (birth_date.month, birth_date.day):
                age -= 1

            if age < 13:
                errors['birth_date'] = "You must be at least 13 years old to register."
                
        if len(first_name) < 2:
            errors['first_name'] = "First name should be at least 2 characters" 
        if len(last_name) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if len(password) < 8:
            errors['password'] = "Password should be at least 8 characters"

        if password != confirm_pw:
            errors['confirm_pw'] = "Passwords do not match."        
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    