from django.conf.urls import patterns, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# General
urlpatterns = patterns('peer_grading.views',
    url(r'^get_next_submission/$', 'get_next_submission'),
    url(r'^save_grade/$', 'save_grade'),
)