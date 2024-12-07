import hashlib
import requests
from io import BytesIO
from PIL import Image
from django.db import models
from rest_framework import serializers, generics, status
from rest_framework.response import Response

# Model Definition
class ImageHash(models.Model):
    image_url = models.URLField(unique=True)
    md5_hash = models.CharField(max_length=32)
    phash = models.CharField(max_length=64)

    def __str__(self):
        return self.image_url
