# Includes URL patterns
from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from authentication import views

app_name = 'auth'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^userLogin/$', views.user_login, name='user_login'),
    url(r'^instruction/$', views.instruction, name='instruction'),
    url(r'^voting/$', views.voting, name='voting'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^candidatevote/$', views.candidatevote, name='candidatevote'),
    url(r'^partyvote/$', views.partyvote, name='partyvote'),

    # Password Reset URLs
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(
        template_name='authentication/password_reset.html',
        email_template_name='authentication/password_reset_email.html',
        success_url=reverse_lazy('auth:password_reset_done'),
    ), name='password_reset'),
    url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password_reset_done.html',
    ), name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/password_reset_confirm.html',
        success_url=reverse_lazy('auth:password_reset_complete'),
    ), name='password_reset_confirm'),
    url(r'^password-reset-complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html',
    ), name='password_reset_complete'),
]
