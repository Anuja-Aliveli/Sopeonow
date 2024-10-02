from django.shortcuts import render
import json

def renderHtml(request):
    return render(request, 'index.html')