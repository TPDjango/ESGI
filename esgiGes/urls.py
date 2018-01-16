from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /esgiGes/
    url(r'^$', views.index, name='index'),
    # ex: /esgiGes/professors/
    url(r'^professors/$', views.results, name='result'),
]
