from rest_framework import serializers
from django.contrib.auth import get_user_model

# from image.serializers import UploadedImageSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # 이미지 업로드 serializer -> 추후 결과물 뽑는 Serializer 로 변경 가능성 있음
    # images = UploadedImageSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ("email", "nickname", "password", "created_at", "deleted_at", "updated_at", "images")
        extra_kwargs = {
            "nickname": {"write_only": True},
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "deleted_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def create(self, validated_data):
        nickname = validated_data.pop('nickname', "이름없음")
        user = User.objects.create_user(nickname=nickname, **validated_data)
        return user
