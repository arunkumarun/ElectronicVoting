from django.conf.urls import url, include
from authentication import views

app_name = 'auth'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^userLogin/$', views.user_login, name='user_login'),
]
