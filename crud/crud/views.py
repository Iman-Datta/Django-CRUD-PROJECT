from django.http import HttpRequest
from django.shortcuts import render

def home(request: HttpRequest):
    if request.method == 'GET':
        context = {'msg1' : 'Welcome to Home',
                   "msg2" : 'CALCULATOR'
                   }
        return render(request,"index.html", context)

def add(request: HttpRequest):
    if request.method == 'POST':
        fNum: int = int(request.POST['firstNumber'])
        sNum: int = int(request.POST['secondNumber'])
        result = fNum+sNum
        print(fNum+sNum)
        return render(request,"add.html", {'result': result})
    
    return render(request,"add.html")

def sub(request: HttpRequest):
    if request.method == 'POST':
        fNum: int = int(request.POST['firstNumber'])
        sNum: int = int(request.POST['secondNumber'])
        result = fNum-sNum
        return render (request,"sub.html",{'result': result})
    
    return render(request,"sub.html")

def multiplication(request: HttpRequest):
    if request.method == 'POST':
        fNum: int = int(request.POST['firstNumber'])
        sNum: int = int(request.POST['secondNumber'])
        result = fNum*sNum
        return render (request,"multiplication.html",{'result': result})
    
    return render(request,"multiplication.html")

def division(request: HttpRequest):
    if request.method == 'POST':
        fNum: int = int(request.POST['firstNumber'])
        sNum: int = int(request.POST['secondNumber'])
        result = fNum/sNum
        return render (request,"division.html",{'result': result})
    
    return render(request,"division.html")