from django.test import TestCase
from users.forms import UserRegisterForm

class TestForms(TestCase):

    def test_user_form_valid_data(self):

        form = UserRegisterForm(data={
            'username': 'user_for_testing',
            'email': 'test_user@gmail.com',
            'password1': 'pass_for_test_1234567',
            'password2': 'pass_for_test_1234567',
        })

        self.assertTrue(form.is_valid())

    def test_user_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)