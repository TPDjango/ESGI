from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /esgiGes/
    url(r'^$', views.index, name='index'),
    # ex: /esgiGes/professors/
    url(r'^professors/$', views.getProfessors, name='professors'),
    # ex: /esgiGes/students/
    url(r'^students/$', views.getStudents, name='students'),
    # ex: /esgiGes/images/
    url(r'^images/$', views.getImages, name='images'),
    # ex: /esgiGes/courses/
    url(r'^courses/$', views.getCours, name='courses'),
]