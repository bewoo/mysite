from django.conf.urls import url

from . import views

app_name = "dump"

urlpatterns = [
    url(r'^(?P<question_id>[0-9]+)/$', views.index, name='detail'),
]

