from django.db import models
import uuid

class item_Model(models.Model):
    item_Name = models.CharField(max_length=250)
    item_Price = models.IntegerField(blank=True, null=True)
    item_Image = models.ImageField(blank=True, null=True)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

