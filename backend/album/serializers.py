from rest_framework import serializers
from .models import Image_collage

class AlbumDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image_collage
        fields = ('user_id', 'result_url', 'img_origin_id', 'created_at', 'deleted_at')


class CollageImageSerializer(serializers.ModelSerializer):
    result_image_id = serializers.IntegerField(source='id')
    result_url = serializers.URLField(required=False)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Image_collage
        fields = ('user_id', 'result_image_id', 'img_origin_id', 'result_url', 'created_at')