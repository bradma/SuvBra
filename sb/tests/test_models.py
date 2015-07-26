from django.test import TestCase

from sb.models import customer

class test_customer_model(TestCase):

    def setUp(self):
        """ Setting up test suite creating models with dummy data """

        record_1 = customer.objects.create(
                id = 0,
                first_name = 'Tester1',
                last_name = 'Test1',
                home_phone = '4326783456',
                cell_phone = '9583885950',
                email = 'x@SuvBra.com',
                full_address = '30 Back Lane',
                city = 'Philadelphia',
                state = 'PA',
                zip_code = '38596',
            )

        record_2 = customer.objects.create(
                id=1,
                first_name = 'Tester2',
                last_name = 'Test2',
                home_phone = '4325364565',
                cell_phone = '4949284858',
                email = 'y@SuvBra.com',
                full_address = '40 Back Lane',
                city = 'Norristown',
                state = 'NJ',
                zip_code = '43678',
            )

    def test_model__not_required(self):
        """ Test Blank Fields """

        record_3 = customer.objects.create(
            id=2,
            first_name = 'Tester2',
            last_name = 'Test2',
            email = 'y@SuvBra.com',
            full_address = '40 Back Lane',
            city = 'Norristown',
            state = 'NJ',
            zip_code = '43678',
        )

    def test_simple_retrieve(self):
        """ test Simple Retrieval of data """

        result = customer.objects.all()
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0].__dict__.keys()), 12)

    def test_model_attributes(self):
        """ Test attributes in customer model """

        result = customer.objects.get(id=0)
        self.assertEqual(result.first_name, 'Tester1')
        self.assertEqual(result.last_name, 'Test1')
        self.assertEqual(result.home_phone, '4326783456')
        self.assertEqual(result.cell_phone, '9583885950')
        self.assertEqual(result.email, 'x@SuvBra.com')
        self.assertEqual(result.full_address, '30 Back Lane')
        self.assertEqual(result.city, 'Philadelphia')
        self.assertEqual(result.state, 'PA')
        self.assertEqual(result.zip_code, '38596')
