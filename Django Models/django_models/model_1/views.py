from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'insert_content': 'Hello I am new here'}
    return render(request, 'model_1/index.html', context = my_dict)
