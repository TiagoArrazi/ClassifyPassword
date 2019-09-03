import unittest
from src.utils.classifier import Classifier


class TestClassifier(unittest.TestCase):

    def test_weak_number(self):
        self.assertEqual(Classifier.classify('12345'), 0)

    def test_weak_lower(self):
        self.assertEqual(Classifier.classify('abcde'), 0)

    def test_weak_upper(self):
        self.assertEqual(Classifier.classify('ABCDE'), 0)

    def test_weak_symbols(self):
        self.assertEqual(Classifier.classify('!@#$%'), 0)

    def test_good_1(self):
        self.assertEqual(Classifier.classify('AAAAAAAAAA'), 1)

    def test_good_2(self):
        self.assertEqual(Classifier.classify('1111111111'), 1)

    def test_good_3(self):
        self.assertEqual(Classifier.classify('!@#$%¨&*()+'), 1)