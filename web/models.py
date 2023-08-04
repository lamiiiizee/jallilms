from django import forms
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField


class Update(models.Model):
    image = VersatileImageField(upload_to="blogs")
    date = models.DateField()
    subhead = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    details = HTMLField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    choices = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = VersatileImageField(upload_to="gallery")
    name = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.name


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return str(self.email)


class Notification(models.Model):
    notification = models.subtitle = models.TextField()

    def __str__(self):
        return self.notification


class PositionsToken(models.Model):
    name = models.CharField(max_length=100)
    fromDateTime = models.DateField(null=True, blank=True)
    toYear = models.DateField(null=True, blank=True)
    subtitle = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
class Award(models.Model):
    image = VersatileImageField(upload_to="awards")
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class YoutubeLink(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-timestamp",)

    def video_url(self):
        return f"https://youtu.be/{self.video_id}"
