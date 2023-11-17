from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from main.models import *
from django.contrib import messages
import uuid
  
id = uuid.uuid1()
print ("hex Representation : ",end="")
trackid=id.hex
print(trackid)
def index(request):
    return render(request,'index.html') 

# take service request
def Tsq(request):
    try:
        if request.method=="POST":
            title=request.POST.get('title')
            desc=request.POST.get('desc')
            uploded_files=request.FILES.get('files')
            randn=uuid.uuid1
            fs= FileSystemStorage()
            data=Details(title=title,desc=desc,files=uploded_files)
            data.save()
            messages.success(request,f'Request successfully submitted! Please save tracking number "{trackid}"')
    except:
            messages.warning(request, 'Please fill form!')

    return render(request,"tsq.html")

def track(request):
    trackid=True
    if trackid == True:
        if request.method=="POST":
            trackid=request.POST.get('trackid')
            data=Track(trackid=trackid)
            data.save()

        messages.success(request,f"your request number {trackid} is successfully reslved")
    else:
        messages.success(request,f"your request num {trackid} will be resolved soon")
    return render(request,"track.html")

def profile(request):
    return render(request,"profile.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def home(request):
    return render(request,"home.html")



