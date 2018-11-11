from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<petition_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<petition_id>[0-9]+)/confirm/(?P<confirmation_hash>.*)$', views.confirm, name='confirm'),
    url(r'^(?P<petition_id>[0-9]+)/get_csv_signature$', views.get_csv_signature, {'only_confirmed': False},
        name='get_csv_signature'),
    url(r'^(?P<petition_id>[0-9]+)/get_csv_confirmed_signature$', views.get_csv_signature, {'only_confirmed': True},
        name='get_csv_confirmed_signature'),
    url(r'^resend/(?P<signature_id>[0-9]+)', views.go_send_confirmation_email, name='resend_confirmation_email'),
    url(r'^(?P<petition_id>[0-9]+)/sign', views.create_signature, name='create_signature'),
    url(r'^org/(?P<org_name>[^/]*)$', views.org_profile, name='org_profile'),
    url(r'^org/(?P<org_name>[^/]*)/dashboard$', views.org_dashboard, name='org_dashboard'),
    url(r'^org/(?P<org_name>[^/]*)/leave$', views.leave_org, name="leave_org"),
    url(r'^org/(?P<org_name>[^/]*)/add_user$', views.org_add_user, name='org_add_user'),
    url(r'^org/(?P<org_name>[^/]*)/new_template$', views.org_new_template, name='org_new_template'),
    url(r'^org/(?P<org_name>[^/]*)/edit_template$', views.org_edit_template, name='org_edit_template'),
    url(r'^org/(?P<org_name>[^/]*)/org_create_petition_template$', views.org_create_petition_template,
        name='org_create_petition_template'),
    url(r'^org/(?P<org_name>[^/]*)/ptemplate_fav_toggle$', views.org_ptemplate_fav_toggle, name='org_ptemplate_fav_toggle'),
    url(r'^user/(?P<user_name>[^/]*)$', views.user_profile, name='user_profile'),
    url(r'^user/(?P<user_name>[^/]*)/dashboard$', views.user_dashboard, name='user_dashboard'),
    url(r'^user/(?P<user_name>[^/]*)/new_template$', views.user_new_template, name='user_new_template'),
    url(r'^user/(?P<user_name>[^/]*)/user_create_petition_template$', views.user_create_petition_template,
        name='user_create_petition_template'),
    url(r'^template_delete$', views.template_delete, name='template_delete'),
    url(r'^get_user_list', views.get_user_list, name='get_user_list'),
    url(r'^invite_accept/$', views.invite_accept, name='invite_accept'),
]