from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /esgiGes/
    url(r'^$', views.index, name='index'),
    # ex: /esgiGes/professors/
    url(r'^professors/$', views.Professors, name='professors'),
    # ex: /esgiGes/students/
    url(r'^students/$', views.Professors, name='professors'),
    # ex: /esgiGes/images/
    url(r'^images/$', views.Professors, name='professors'),
    # ex: /esgiGes/courses/
    url(r'^courses/$', views.Professors, name='professors'),
]
