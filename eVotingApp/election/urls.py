# Includes Url PAtterns

from django.conf.urls import url, include

from authentication import views
from election import views as eView

# Includes home page to Url
urlpatterns = [
    url(r'^$', views.home, name='home')
]