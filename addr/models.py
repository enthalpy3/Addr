from django.db import models
from django.utils import timezone


class Addr(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # published_date = models.DateTimeField(blank=True, null=True)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # on_off = models.NullBooleanField(default=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name