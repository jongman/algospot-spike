# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
import judge.views

urlpatterns = patterns('',
    url(r'$', 'judge.views.index', name='judge_index')
)

