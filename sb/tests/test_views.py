from django.test import SimpleTestCase, RequestFactory

class test_my_views(SimpleTestCase):
	def setUp(self):
		self.factory = RequestFactory()

	def test_view(self):
		...