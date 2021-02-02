from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^logout/$',views.logout_request,name="logout"),



]