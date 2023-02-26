from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    '''create object for destination class of model file here'''
    # desc1= Destination()
    # desc1.name="Mumbai"
    # dests = [desc1,desc2,desc3]
    # return render(request,"index.html",{'desc1':desc1})
    dests = Destination.objects.all()
    
    return render(request,"index.html",{'dests':dests})
# give price dynamically
    # return render(request,"index.html",{'price':500})