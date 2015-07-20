from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView


urlpatterns = patterns('',

                       url(r'^$',
                           TemplateView.as_view(template_name='index.html'),
                           name='index'),
                       url(r'^enroll/$',
                           TemplateView.as_view(template_name='enroll.html'),
                           name='enroll'),
                          )
