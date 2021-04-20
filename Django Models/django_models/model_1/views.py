from django.shortcuts import render
from model_1.models import AccessRecord, Webpage, Topic
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request, 'model_1/index.html', context = date_dict)
