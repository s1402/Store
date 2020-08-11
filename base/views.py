from django.shortcuts import render
from .models import Todaysspecial
# Create your views here.

def index(request):
    todays=Todaysspecial.objects.all()
    return render(request,'index.html',{'todays':todays})