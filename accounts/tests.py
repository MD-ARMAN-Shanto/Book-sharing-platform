from django.test import TestCase
from .models import BookList

class Booklist(TestCase):
    def setUp(self):
        BookList.objects.create(name="lion", sound="roar")
        BookList.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        book1 = BookList.objects.get(name="hello_world")
        book2 = BookList.objects.get(name="welcome to django world")
        self.assertEqual(book1.write(), 'The lion says "travis"')
        self.assertEqual(book2.write(), 'The cat says "shakespeer"')
