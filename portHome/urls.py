from django.conf.urls import url

from portHome import views

app_name = 'portHome'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about_me, name='about'),
    url(r'^details/(?P<project_id>[0-9]+)/$', views.project_details, name='details')
]
