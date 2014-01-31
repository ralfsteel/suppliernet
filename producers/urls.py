from producers import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.customer, name='customer'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'))
