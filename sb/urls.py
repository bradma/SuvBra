from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from sb.views import first_view, customer_detail, main_logout

urlpatterns = [
    url(r'^logout/', main_logout, name='logout'),
	url(r'^$', login_required(first_view.as_view()), name='concept_1'),
    url(r'customerDetailed/(?P<pk>\d+)/$', login_required(customer_detail.as_view()), name='customer-detail'),
]