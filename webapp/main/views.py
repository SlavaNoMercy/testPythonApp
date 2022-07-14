from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'main/main.html')


def about(request):
    return HttpResponse('<h4>About</h4>')
