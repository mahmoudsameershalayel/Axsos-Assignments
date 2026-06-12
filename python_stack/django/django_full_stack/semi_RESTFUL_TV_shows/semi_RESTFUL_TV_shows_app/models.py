from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        title = postData.get('title', '').strip()
        network = postData.get('network', '').strip()
        description = postData.get('description', '').strip()
        release_date = postData.get('release_date')

        if Show.objects.filter(title__iexact=title).exclude(id=postData.get('id')).exists():
            errors['title'] = "A TV show with this title already exists."

        if release_date:
            release_date = date.fromisoformat(release_date)
            if release_date > date.today():
                errors['release_date'] = "Release date must be in the past."
        if len(title) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(network) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if description and len(description) < 10:
            errors['description'] = "Description should be at least 10 characters"
        
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    