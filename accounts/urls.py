from django.conf.urls import url

from accounts.views import UserprofileList, UserprofileDetalhe, UserprofileUpdate, userprofile_delete

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from accounts import views as accounts_views


app_name = 'accounts'

urlpatterns = [

    url(r'^userprofile-list/$', UserprofileList.as_view(), name='userprofile-list'),
    url(r'^userprofile-list/(?P<pk>[0-9]+)/$', UserprofileDetalhe.as_view(), name='userprofile-detail'),
    url(r'^userprofile/(?P<pk>[0-9]+)/edit/$', UserprofileUpdate.as_view(), name='userprofile-edit'),
    url(r'^userprofile/(?P<id>[0-9]+)/delete/$', userprofile_delete, name='userprofile-delete'),

    #
    # AUTENTICAÇÃO
    #
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', accounts_views.signup, name='signup'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'), name='password_change_done'),

]
