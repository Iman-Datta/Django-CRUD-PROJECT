from django.http import HttpRequest
from django.shortcuts import render

def home(request: HttpRequest):
    if request.method == 'GET':
        msg: str = 'Welcome to Home'
        return render(request,"index.html", {'message': msg})

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

def multiplecation(request: HttpRequest):
    if request.method == 'POST':
        fNum: int = int(request.POST['firstNumber'])
        sNum: int = int(request.POST['secondNumber'])
        result = fNum*sNum
        return render (request,"sub.html",{'result': result})
    
    return render(request,"multiplication.html")