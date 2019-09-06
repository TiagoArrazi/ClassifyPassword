import unittest
from src.utils.classifier import Classifier


class TestClassifier(unittest.TestCase):

    def test_weak_1(self):
        self.assertEqual(Classifier.classify('aabc'), 0)

    def test_weak_2(self):
        self.assertEqual(Classifier.classify('aaaaaaaa'), 0)

    def test_weak_3(self):
        self.assertEqual(Classifier.classify('abcdefgh'), 0)

    def test_good_1(self):
        self.assertEqual(Classifier.classify('13254afgds'), 1)

    def test_good_2(self):
        self.assertEqual(Classifier.classify('3RgTaaaa$123'), 1)

    def test_good_3(self):
        self.assertEqual(Classifier.classify('aaaa123DD'), 1)

