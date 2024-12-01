from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, Django!, Home")
    return render(request, "website/index.html")

def about(request):
    # return HttpResponse("Hello, Django!, about")
    return render(request, "website/about.html")
def contact(request):
    return HttpResponse("Hello, Django!, contact")