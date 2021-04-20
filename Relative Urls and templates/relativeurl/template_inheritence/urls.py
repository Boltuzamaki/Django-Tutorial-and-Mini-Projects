from django.conf.urls import url
from template_inheritence import views

urlpatterns = [
    url('^$', views.index, name='index3'),
    url('^other/$', views.other, name='other'),
]
