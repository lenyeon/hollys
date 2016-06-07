from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
                url(r'^login/$', login, name = 'login'),
                url(R'^signup/$', views.signup, name='signup'),
                url(r'^logout/$', logout, name='logout'),
                url(r'^signup/$', views.signup, name='signup'),
]
