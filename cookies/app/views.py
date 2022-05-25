from urllib import response
from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.

def setcookie(request):
    response = render(request,'app/setcookies.html')
    # response.set_cookie('name','alok',max_age=60) #expire after 60 sec
    response.set_cookie('name','alok',expires=datetime.utcnow()+timedelta(days=2))  #expires after 2 days
    return response

def getcookie(request):
    # name=request.COOKIES['name']       # // method 1
    # name = request.COOKIES.get('name')   #// method 2
    name = request.COOKIES.get('name','Guest')
    return render(request,'app/getcookies.html',{'name':name})

def delcookie(request):
    response=render(request,'app/delcookies.html')
    response.delete_cookie('name')
    return response