from django.test import TestCase

from sb.forms import customer_form

class test_customer_forms(TestCase):

    def setUp(self):
        self.form = customer_form()
        self.fields_should_be_there = [
            'first_name',
            'last_name',
            'home_phone',
            'cell_phone',
            'email',
            'full_address',
            'alt_address',
            'city',
            'state',
            'zip_code',
        ]

    def test_customer_form__is_valid(self):
        """ Test Form renders correctly """

        self.assertTrue(self.form.is_valid)

    def test_customer_form__attributes(self):
        self.assertEqual(len(self.form.fields.keys()), 10)
        self.assertEqual(self.form.as_table().count('label'), 20)
        try:
            for check in self.fields_should_be_there:
                self.form.fields[check]
        except KeyError as ex:
            self.fail(ex)