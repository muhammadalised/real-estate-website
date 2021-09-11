from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'page': 'index',
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'page': 'about'
    }
    return render(request, 'pages/about.html', context)
