from nose.tools import eq_

from django.test import TestCase


class SampleTest(TestCase):

    def test_adder(self):
        eq_(1 + 1, 2)
