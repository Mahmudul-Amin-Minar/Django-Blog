from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='home'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add/$', views.add_post, name='post_create'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_post, name='delete'),
    url(r'^edit/(?P<id>\d+)/$', views.edit_post, name='edit'),
    url(r'^my-posts/$', views.my_posts, name='my_posts'),
]