import unittest

from enum_samples.enum import SampleEnum, LegalFormUS


class MyTestCase(unittest.TestCase):
    def test_enum_values(self):
        sample_enum_values = [item.value for item in SampleEnum]
        legal_form_us_values= [item.value for item in LegalFormUS]

        self.assertIsNotNone(sample_enum_values)
        self.assertIsNotNone(legal_form_us_values)
        print(sample_enum_values)
        print(legal_form_us_values)
