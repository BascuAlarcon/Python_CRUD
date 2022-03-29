from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def init(request):
    return HttpResponse("<h1>Welcome to Django!</h1>")
def contact(request):
    return render(request, 'pages/contact.html')