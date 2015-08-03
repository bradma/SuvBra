from django.conf.urls import include, url

from sb.views import first_view, customer_detail

urlpatterns = [
	url(r'^$', first_view.as_view(), name='concept_1'),
    url(r'(?P<user_pk>\d+)^$', customer_detail.as_view(), name='customer-detail'),
]