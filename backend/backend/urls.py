from django.conf.urls import url, include
from rad.views import *

urlpatterns = [
  url(r'^rad/states_daily', states_daily),
  url(r'^rad/usa_daily', usa_daily),
  url(r'^rad/get_states/$', get_states),
  url(r'^rad/get_usa/$', get_usa)
]
