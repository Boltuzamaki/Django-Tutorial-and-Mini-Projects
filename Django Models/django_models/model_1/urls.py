from django.conf.urls import url
from model_1 import views
urlpatterns = [
 url(r'^$', views.index, name='index'),
]
