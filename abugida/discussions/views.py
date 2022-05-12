from django.shortcuts import render
from django.http import HttpResponse


def discussions(request):
    return render(request, 'discussions/discussions.html')

