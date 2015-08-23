from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin

from sb.views import cust_viewset, login_view

router = routers.DefaultRouter()
router.register(r'customers', cust_viewset)

urlpatterns = patterns('',
    url(r'^$', login_view.as_view(), name='login'),
	url(r'^Concept/', include('sb.urls', namespace='test')),
    url(r'^api/', include(router.urls, namespace='rest_api')),
    url(r'^admin/', include(admin.site.urls)),
)
