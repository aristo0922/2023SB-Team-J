import pickle
import time
import json
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .AiTask import *
from .s3_utils import *
from .models import *
from rest_framework.permissions import AllowAny

from album.serializers import *


class UploadImageView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        image = request.data.get("image")
        user_id = request.data.get("id")
        with Image.open(image) as im:
            im = im.convert("RGB")
            im_jpeg = BytesIO()
            im.save(im_jpeg, 'JPEG')
            im_jpeg.seek(0)
        key = "image_upload/" + generate_unique_filename(im_jpeg.getvalue()) + ".jpeg"
        img_url = upload_image_to_s3(im_jpeg, key, ExtraArgs={'ContentType': "image/jpeg"})
        data ={
            "user_id": user_id,
            "url": img_url
        }
        serializer = UploadedImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "origin_img_id": serializer.data["id"],
                "url": serializer.data["url"]
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, format=None):
#         raw_data = request.body.decode('utf-8')
#         try:
#             data = json.loads(raw_data)
#             user_id = data.get('user_id')
#             source = data.get('source')

#             if user_id is None or source is None:  # request 형식에 맞지 않는 경우
#                 return Response(status=status.HTTP_400_BAD_REQUEST)

#             image_origin = Image_upload.objects.get(id=source, user_id=user_id, deleted_at__isnull=True)

#         except:
#             # 찾지 못한 경우 HTTP_400
#             return Response(status=status.HTTP_400_BAD_REQUEST)


#         serializer = UploadedImageSerializer(image_origin)

#         picture = {
#             'url_1': serializer.data.get('url_1'),
#             'url_2': serializer.data.get('url_2'),
#             'url_3': serializer.data.get('url_3'),
#             'url_4': serializer.data.get('url_4'),
#         }
#         return Response(picture, status=status.HTTP_200_OK)

class AiExecute(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        url = request.data.get("image")
        id = request.data.get("image_origin_id")
        task1 = model1_execute.delay(url, id)
        task2 = model2_execute.delay(url, id)
        task3 = model3_execute.delay(url, id)

        while True:
            if task1.ready() and task2.ready() and task3.ready():
                break
            time.sleep(1)
        if task1.result and task2.result and task3.result:
            response = {**task1.result, **task2.result, **task3.result}

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#sudo celery -A backend_project.celery multi start 4 --loglevel=info --pool=threads
#sudo celery multi stop 4 -A backend_project.celery --all
    def patch(self, request):
        select = request.data.get("select", [])
        select_id = request.data.get("select_id", [])
        data ={
            "is_selected": True
        }
        for i, id in zip(select, select_id):  # zip 함수를 사용하여 두 리스트를 병렬로 묶음
            if i == 1:
                model = Image_upload.objects.get(id=id)
                serializer = UploadedImageSerializer(model, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                model = Ai_model.objects.get(id=id)
                serializer = Ai_modelSerializer(model, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
           
class ResultImageView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user_id = request.data.get("user_id")
        result_image = request.data.get("result_image")
        im = Image.open(result_image)
        im = im.convert("RGB")
        im_jpeg = BytesIO()
        im.save(im_jpeg, 'JPEG')
        im_jpeg.seek(0)
        key = "Result_image/" + generate_unique_filename(im_jpeg.getvalue()) + ".jpeg"
        img_url = upload_image_to_s3(im_jpeg, key, ExtraArgs={'ContentType': "image/jpeg"})

        data = {
            "user_id": user_id,
            "result_url": img_url
        }

        serializer = ResultImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)