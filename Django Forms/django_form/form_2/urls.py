from django.conf.urls import url
from form_2 import views

urlpatterns =[
        url(r'^$', views.index, name='index2'),
        url(r'^user/', views.user, name='user_view'),
]
