from django.db import models

class Comments(models.Model):
    user_id = models.IntegerField(default=0)
    house_id = models.IntegerField()
    description = models.CharField(max_length=280)
