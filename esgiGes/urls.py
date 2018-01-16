
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^professors/(?P<id>\d+)/$', views.get_professor, name="get_professor")
]