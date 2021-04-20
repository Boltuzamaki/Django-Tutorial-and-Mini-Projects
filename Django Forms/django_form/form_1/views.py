from django.shortcuts import render
from form_1 import forms
# Create your views here.


def index(request):
    return render(request, 'form_1/index.html')

def form_name_view(request):
    form = forms.FormName(request.POST)

    if form.is_valid():
        print('VALIDATION SUCCESS')
        print("NAME: "+ form.cleaned_data['name'])
        print("EMAIL: "+ form.cleaned_data['email'])
        print("TEXT: "+form.cleaned_data['text'])
    return render(request, 'form_1/form.html', {'form':form})
