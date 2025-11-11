from django.shortcuts import render
def view(request,room_name):
    return render(request,"index.html",{"roomname":room_name})
# Create your views here.
