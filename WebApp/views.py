from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User


# Create your views here.


# def test_01(request):
#
#     html = "<html><body>hello word<body></html>"
#     # return HttpResponse(html)
#     # return HttpResponseNotFound('<h1>Page not found</h1>')
#     return HttpResponse(status=404)

def test_user(request):
    user_list = User.objects.all()
    for i in user_list:
        print i
    return render_to_response('user_list.html', {'user_list': user_list})
