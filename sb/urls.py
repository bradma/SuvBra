from django.conf.urls import include, url

from sb.views import first_view, customer_detail, login_view

urlpatterns = [
    url(r'^login/', login_view.as_view(), name='login'),
	url(r'^$', first_view.as_view(), name='concept_1'),
    url(r'customerDetailed/(?P<pk>\d+)/$', customer_detail.as_view(), name='customer-detail'),
]