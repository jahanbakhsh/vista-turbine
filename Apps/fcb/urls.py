from django.conf.urls import url
from Apps.loder.views import FCBIndex
from Apps.fcb.views import RetriveNews, RetrivePlayerList


urlpatterns = [
    url(r'^$',FCBIndex),
    url(r'^/news$',RetriveNews.as_view()),
    url(r'^/player/list$', RetrivePlayerList.as_view()),
]