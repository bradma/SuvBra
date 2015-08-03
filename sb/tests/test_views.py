from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from sb.views import first_view, customer_detail

from sb.models import customer

class test_my_views(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        customer.objects.create(
            first_name= 'Test',
            last_name= 'Me',
            home_phone= '2549583453',
            email = 'x@skip.com',
            full_address = '320 Charlies Lane',
            city = 'Philly',
            state = 'PA',
            zip_code = '39434'
        )

    def test_customer_detail__status_code(self):
        """ Test that customer detail is status 200 """

        url = reverse('test:customer-detail', kwargs={'pk': 1})
        request = self.factory.get(url)
        response = customer_detail.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_first_view__status_code(self):
        """ Test that Concept view is rendering """

        url = reverse('test:concept_1')
        request = self.factory.get(url)
        response = first_view.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_first_view__returned_context(self):
        """ Test the correct context is being returned """

        url = reverse('test:concept_1')
        request = self.factory.get(url)
        response = first_view.as_view()(request)
        try:
            for test_context in ['form', 'customer_info']:
                response.context_data[test_context]
        except KeyError as ex:
            self.fail(ex)

    def test_first_view__template_correct(self):
        """ Test view is looking at correct template """

        url = reverse('test:concept_1')
        request = self.factory.get(url)
        response = first_view.as_view()(request)
        self.assertEqual(response.template_name[0], 'suvbra/home.html')