from django.shortcuts import render,HttpResponse


# Create your views here.

def home(request):
    #return HttpResponse('<h1>Hello we are here in lamzing</h1>')
    return render(request, 'htmlfiles/home.html')


def reg(request):
    name = 'Bidyachandra'
    address1 = 'Singjamei'
    num = [11,22,33,44,55,66,77,88,99,100]
    p = {'name':name,'add':address1,'number1':num}
    #return HttpResponse('hello this is the registration page')
    return render(request,'registration.html',p)


def cal(request):
     return render(request,'calculatorformat.html')

def java(request):
     return render(request,'class2.html')