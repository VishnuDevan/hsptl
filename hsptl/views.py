from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def HELLO(request):
    return HttpResponse("HELLO")

def hello(request):
    return render(request,"hsptl/hsptl.html")

def hai(request):
    return render(request,"hsptl/snd.html")
def newpage(request):
    return render(request,"hsptl/newpage.html")
