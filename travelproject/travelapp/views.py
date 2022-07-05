from django.http import HttpResponse
from django.shortcuts import render
from  .models import place
from .models import  team
from django.contrib.auth.models import User


def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})


#def about(request):
   # return render('about.html')

