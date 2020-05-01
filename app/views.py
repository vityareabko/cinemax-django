from django.shortcuts import render
# from .models import Film

def index(request):
    return render(request, 'app_template/homepage.html')