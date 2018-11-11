from django.shortcuts import render,HttpResponse,get_object_or_404
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect

# class Index():
#
#
#     def get(self, request, *args, kwargs):
#         index_page = 'index.html'
#         return HttpResponse(index_page)
#         # return render(request , index_page)
def Index(re):
    index_page = 'index.html'
    print(settings.STATIC_ROOT)
    # return HttpResponse(index_page)
    return render(re , index_page)