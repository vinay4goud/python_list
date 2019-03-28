from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Assets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True, default=None)
    c_on = models.DateTimeField()
    tags = models.CharField(max_length=250)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}-{self.is_sold}"


class AssetRawData(models.Model):
    c_on = models.DateTimeField()
    mobile_no = models.CharField(max_length=20, null=True, blank=True, default=None)
    content = models.CharField(max_length=1500, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.pk}-{self.mobile_no}"

