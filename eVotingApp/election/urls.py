from django.conf.urls import url, include

from authentication import views
from election import views as eView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^info/', eView.info, name='info'),
]