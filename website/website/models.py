from django.db import models

class Nav(models.Model):
    slug = models.CharField(max_length=50)
    content = models.TextField()
