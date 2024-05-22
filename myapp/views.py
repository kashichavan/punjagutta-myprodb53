from django.shortcuts import render
from .models import Student
# Create your views here.

def getdata(request):
    data=Student.objects.all()
    return render(request,'h1.html',context={'data':data})

