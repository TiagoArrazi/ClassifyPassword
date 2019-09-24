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
        self.assertEqual(Classifier.classify('sfdsdfsd33257'), 1)

    def test_good_2(self):
        self.assertEqual(Classifier.classify('3RgTaaaa$123'), 1)

    def test_good_3(self):
        self.assertEqual(Classifier.classify('0351garttb'), 1)

    def test_strong_1(self):
        self.assertEqual(Classifier.classify('ah5@gn/4@%7U2F3'), 2)

    def test_strong_2(self):
        self.assertEqual(Classifier.classify('89?>2&2/v>[7c&a7.5ts6}2,=g+D'), 2)

    def test_strong_3(self):
        self.assertEqual(Classifier.classify('5mgYm}jUy4pO0fl2gV94IK5~'), 2)

