import uuid
from django.conf import settings
from django.db import models
from django.db.models import signals
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from main_app.models import Niche
from datetime import datetime

def upload_path_handler(instance, filename):
    if instance.__class__.__name__ == "Campaign":
        return "user_images/brand_images/{id}/campaign_images/{filename}".format(filename=filename + str(datetime.now().time()), id=instance.brand.id)
    elif instance.__class__.__name__ == "Brand":
        return  "user_images/brand_images/{id}/{filename}".format(filename=filename, id=instance.id)
    elif instance.__class__.__name__ == "BrandManagerProfile":
        return "user_images/user_profile_images/{id}/{filename}".format(filename=filename + str(datetime.now().time()), id=instance.user.id)
    else:
        return "user_images/not_sorted/{id}/{filename}".format(filename=filename, id=instance.id)

class BrandManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    managers = models.ManyToManyField(BrandManagerProfile)
    image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
    info = models.TextField()

    def __str__(self):
        return self.name

class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
    goals = models.TextField()
    target_audience = models.TextField()
    detailed_description = models.TextField()
    niches = models.ManyToManyField(Niche)
    budget = models.PositiveIntegerField()
    submission_deadline = models.DateField(auto_now=False, auto_now_add=False,)
    posted = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.brand.name + ": " + self.name