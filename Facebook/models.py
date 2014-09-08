from django.db import models
from django.db import models 
from django.dispatch.dispatcher import receiver 
from django_facebook.models import FacebookModel 
from django.db.models.signals import post_save 
from django_facebook.utils 
import get_user_model, get_profile_model 
from your_project import settings

# Create your models here.

class FacebookProfile(FacebookModel):
    Fbuser = models.OneToOneField(settings.AUTH_USER_MODEL)
    
    @receiver(post_save)
    def create_profile(sender, instance, created, **kwargs):
        if sender == get_user_model():
            Fbuser = instance
            profile_model = get_profile_model()
            if profile_model == FacebookProfile and created:
                profile, new = FacebookProfile.objects.get_or_create(user=instance)
