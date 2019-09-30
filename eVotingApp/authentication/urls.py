from django.contrib.auth import views
from django.urls import path, re_path

urlpatterns = [
    re_path('login/', views.LoginView.as_view(), name='login'),

]
