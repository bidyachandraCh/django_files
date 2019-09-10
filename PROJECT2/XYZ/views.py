from django.shortcuts import render

# Create your views here.
def gall(request):
    return render(request,'gallery.html')