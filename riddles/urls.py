from django.urls import re_path, path
from .views import *

# app_name = 'riddles'
urlpatterns = [
    # path('', index),
    re_path(r'^$', index, name='index'),
    re_path(r'^([0-9]+)/$', detail, name='detail'),
    re_path(r'^([0-9]+)/answer/$', answer, name='answer'),
    re_path(r'^register/$', RegisterFormView.as_view()),
    re_path(r'^login/$', LoginFormView.as_view()),
    re_path(r'^logout/$', LogoutView.as_view()),
    re_path(r'^password-change/', PasswordChangeView.as_view()),
    re_path(r'^([0-9]+)/post/$', post, name='post'),
    re_path(r'^([0-9]+)/msg_list/$', msg_list, name='msg_list'),
    re_path(r'^([0-9]+)/post_mark/$', post_mark, name='post_mark'),
    re_path(r'^([0-9]+)/get_mark/$', get_mark, name='get_mark'),
    re_path(r'^admin/$', admin, name='admin'),
    re_path(r'^post_riddle/$', post_riddle, name='post_riddle'),
]

