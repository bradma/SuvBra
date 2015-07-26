from django.test import SimpleTestCase, RequestFactory
from django.core.urlresolvers import reverse

from sb.views import first_view

class test_my_views(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

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