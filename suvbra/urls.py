from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^Concept/', include('sb.urls', namespace='test')),
	url(r'^admin/', include(admin.site.urls)),
)
