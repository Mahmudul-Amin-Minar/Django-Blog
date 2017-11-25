from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

app_name = 'register'

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'register/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'register/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^change-password/$', views.change_password, name='change_password'),

]
