from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    message = "<html><body><em>This is second project</em></body></html>"
    return HttpResponse(message)
