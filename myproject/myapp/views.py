import requests
from io import BytesIO
from PIL import Image
from rest_framework import  generics, status
from rest_framework.response import Response
from .models import ImageHash
from .serializers import ImageHashSerializer
from .utils import calculate_md5, calculate_phash

# API Views

class ImageHashCreateView(generics.CreateAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer

    def create(self, request, *args, **kwargs):
        image_url = request.data.get('image_url')

        # Fetch the image content
        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return Response({'error': f'Unable to fetch image: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        image_content = response.content

        # Calculate hashes
        md5_hash = calculate_md5(image_content)
        try:
            image = Image.open(BytesIO(image_content))
            phash = calculate_phash(image)
        except Exception as e:
            return Response({'error': f'Error processing image: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to database
        serializer = self.get_serializer(data={
            'image_url': image_url,
            'md5_hash': md5_hash,
            'phash': phash
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ImageHashListView(generics.ListAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer

class ImageHashDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer

