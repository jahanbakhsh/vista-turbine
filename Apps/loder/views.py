from django.shortcuts import render,HttpResponse,get_object_or_404


def Index(request):
    index_page = 'index.html'
    return render(request , index_page)

def FCBIndex(request):
    index_page = 'fcb-index.html'
    return render(request , index_page)