from django.shortcuts import render
from django.http import HttpResponse

def yohaanHello(request):
    return HttpResponse("Hello Yohaan")

def call_html(request):
    return render(request, "hello.html")