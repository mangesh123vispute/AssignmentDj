from rest_framework import serializers
from .models import ImageHash

class ImageHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHash
        fields = ['id', 'image_url', 'md5_hash', 'phash']
        read_only_fields = ['md5_hash', 'phash']