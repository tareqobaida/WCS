from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,template_name="index.html")
    # return HttpResponse("Hello, world. You're at the polls index.")