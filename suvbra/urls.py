from django.conf.urls import patterns, include, url
from rest_framework import routers

from sb.views import cust_viewset

router = routers.DefaultRouter()
router.register(r'customers', cust_viewset)

urlpatterns = patterns('',
	url(r'^Concept/', include('sb.urls', namespace='test')),
    url(r'^api/', include(router.urls, namespace='rest_api')),
)
