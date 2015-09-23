from django.core.urlresolvers import reverse
from django.test import TestCase


class HomeTests(TestCase):

    def test_base(self):
        response = self.client.get(reverse('home'))
        assert b'csrfmiddlewaretoken' in response.content
