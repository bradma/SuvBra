from django.conf.urls import include, url

from sb.views import first_view

urlpatterns = [
	url(r'^$', first_view.as_view(), name='concept_1'),
]