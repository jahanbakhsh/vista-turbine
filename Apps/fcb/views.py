from lib.util import BaseAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Apps.fcb.models import *
from rest_framework.generics import ListAPIView
from Apps.fcb.serializers import PlayerListSerializer


class RetriveNews(APIView, BaseAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            news_type = request.GET.get('type',None)
            news =[]
            index = -1
            type = News._meta.get_field('type').choices
            for item in type:
                if item[1]==news_type:
                    index=item[0]

            if index>0:
                for item in News.objects.filter(type=index):
                    news.append({
                        'title':item.title,
                        'large_img': item.large_img.url,
                        'small_img': item.small_img.url,
                        'source':item.source,
                        'content':item.content,
                    })

                self.response.data=news
                self.response.status_code=200
                return Response(self.response.as_dict(), headers={'Access-Control-Allow-Origin': '*'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

class RetrivePlayerList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PlayerListSerializer
    queryset = Player.objects.all()

