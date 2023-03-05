from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profles/', default='profiles/default.png')
    username = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)


    def __str__(self) -> str:
        return self.name