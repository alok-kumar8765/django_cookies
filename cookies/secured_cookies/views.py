from email.policy import default
from urllib import response
from django.shortcuts import render

# Create your views here.
def setsignedcookie(request):
    response = render(request,'app/setcookies.html')
    response.set_signed_cookie('name','alok',max_age=60,salt='name')
    return response

def getsignedcookie(request):
    name=request.get_signed_cookie('name',salt='name',default='Guest')
    return render(request,'app/getcookies.html',{'name':name})

def deletesignedcookie(request):
    response=render(request,'app/delcookies.html')
    response.delete_cookie('name')
    return response

# salt = "" must be same in set and get, if it is not same then error comes in that case use default