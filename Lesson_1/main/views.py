from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def user_profile(request):
    return render(request, 'main/user_profile.html')


def contact(request):
    return render(request, 'main/contact.html')


def content(request):
    return render(request, 'main/content.html')

def news_page(request):
    return render(request, 'main/news_page.html')
