from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def TestFn(request) :
 return HttpResponse('helooooooo')
def hometest(request) :
  return HttpResponse('<h1> home </h1>') 
def html1(request) :
  return render(request,'forms.html')