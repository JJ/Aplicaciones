from django.conf.urls import patterns, url

from empresas import views
from empresas.views import current_datetime, hours_ahead

urlpatterns = patterns('',
    	 url(r'^$', views.index, name='index'),
	 url(r'^time/$', current_datetime),
	 url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
