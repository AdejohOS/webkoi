from django.db import models

from django.utils.text import slugify

import uuid

# tinymce


# Create your models here.


class Message(models.Model):
    VENUE = (
        ('Koinonia, Zaria', 'Koinonia, Zaria'),
        ('Koinonia, Abuja', 'Koinonia, Abuja'),
        ('External Ministration', 'External Ministration')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    preacher = models.CharField(max_length=200, null=True, blank=True)
    minister = models.ForeignKey('Minister', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', blank=True)
    location = models.CharField(max_length=200, blank=True, choices=VENUE)
    message_year = models.CharField(max_length=4, null=True, blank=True)
    message_audio = models.FileField(upload_to='audio/')
    message_image = models.ImageField(upload_to='message-img/', null=True, blank=True, default='default.jpg')
    message_date = models.DateField(auto_now_add=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Minister(models.Model):
    minister_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.minister_name


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.category_name
