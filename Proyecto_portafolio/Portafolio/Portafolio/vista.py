"""
WSGI config for Portafolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

from django.shortcuts import render

def index(request):
    return render(request,'index.html')