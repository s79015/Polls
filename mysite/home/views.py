from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.http import HttpResponse
import logging

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/main.html', context)

logger = logging.getLogger(__name__)

# Create your views here.

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    
    # return HttpResponse('view count='+str(num_visits))
    response = HttpResponse(response+'view count='+str(num_visits))  
    response.set_cookie('dj4e_cookie', 'b0e864a6', max_age=1000)
    return response

def owner_home(request):
    
       return HttpResponse("Hello, world. b0e864a6 is the polls index.")

def helloworld_2(request):
    
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    
    # return HttpResponse('view count='+str(num_visits))
    response = HttpResponse('view count='+str(num_visits))  
    response.set_cookie('dj4e_cookie', 'b0e864a6', max_age=1000)
    return response

def hello(request):
    # view_count = request.COOKIES.get('dj4e_cookie') + 1
    response = HttpResponse('dj4e_cookie')
    response.set_cookie('dj4e_cookie','b0e864a6', max_age=1000)

    if request.COOKIES.get('dj4e_cookie') is not None:
        value = request.COOKIES.get('dj4e_cookie')
        response = HttpResponse('view count='+str(value)) 
        response.set_cookie('dj4e_cookie', int(value) + 1)
        return response
    else:
        return redirect('/hello/hello')
    