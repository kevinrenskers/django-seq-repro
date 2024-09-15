from django.test import TestCase

from .models import Content


class ContentTests(TestCase):
    def test(self):
        content = Content.objects.create(name="One")
        self.assertEqual(content.pk, 50001)
