from django.conf.urls import url
from Apps.employment.views import Hierd

urlpatterns = [
    url(r'^add/hierd/', Hierd.as_view()),
]