import string

from django.db import models

class UrlData(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    new_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Short Url for: {self.url} is {self.new_url}"

    class Meta:
        verbose_name_plural = 'Urls'
        verbose_name = 'Url'

