import unittest
from email_validator import *


class TestEmailValidator(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email("nick.kim@gmail.com"))
        self.assertTrue(validate_email("hello-world@yahoo.com"))
        self.assertFalse(validate_email("nick.com@gmail"))
        self.assertFalse(validate_email("nick kim@gmail.com"))
