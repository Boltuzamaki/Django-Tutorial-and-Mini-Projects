from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'template_inheritence/index.html')

def other(request):
    return render(request, 'template_inheritence/other.html')
