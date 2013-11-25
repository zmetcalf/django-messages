from django.contrib import messages
from django.shortcuts import render

def index(request):
    messages.info(request, 'Hello world.')
    messages.success(request, 'Goodbye world.')
    return render(request, 'index.html', {})
