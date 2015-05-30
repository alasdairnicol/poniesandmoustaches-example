import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Conference

def index(request):
    """
    Homepage
    """
    return render(request, "index.html", {})

def view_conferences(request):
    """
    View all of the conferences in one page
    """
    engine = request.GET.get('engine', 'django')
    conferences = Conference.objects.all()
    if engine == "mustache":
        conferences = conferences.values()
    return render(request, "view_conferences.html", {'conferences': conferences}, using=engine)

def view_conferences_json(request):
    """
    Returns the conferences in json format
    """
    out = {'conferences': list(Conference.objects.all().values())}
    return JsonResponse(out)
