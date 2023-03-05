from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem
from .sms import send_sms

@receiver(post_save, sender=OrderItem)
def create_profile(sender, instance, created, **kwargs):
    
    if OrderItem.prepared:
        send_sms()