from django.conf.urls import url

from portHome import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
