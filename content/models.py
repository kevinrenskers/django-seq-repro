from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=255, blank=True)
    is_readonly = models.BooleanField(default=False)
