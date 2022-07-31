from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
from django.utils.text import slugify


class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.slug = slugify(self.target_url)
        super(Link, self).save(*args, **kwargs)
