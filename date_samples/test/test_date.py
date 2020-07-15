import unittest
from datetime import date

from enum_samples.enum import SampleEnum, LegalFormUS


class MyTestCase(unittest.TestCase):
    def test_get_date_from_epoch(self):
        epoch: int = 1594771200  # Wed, 15 Jul 2020 00:00:00 GMT
        d = date.fromtimestamp(epoch)

        self.assertIsNotNone(d)
        print(f'{epoch} == {d}')
