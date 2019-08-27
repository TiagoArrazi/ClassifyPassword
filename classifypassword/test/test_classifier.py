import unittest
from src.utils.classifier import Classifier


class TestClassifier(unittest.TestCase):

    def test_very_weak_1(self):
        self.assertEqual(Classifier.svm_classify(), 0)

    def test_very_weak_2(self):
        self.assertEqual(Classifier.svm_classify(), 0)

    def test_very_weak_3(self):
        self.assertEqual(Classifier.svm_classify(), 0)

    def test_weak_1(self):
        self.assertEqual(Classifier.svm_classify(), 1)

    def test_weak_2(self):
        self.assertEqual(Classifier.svm_classify(), 1)

    def test_weak_3(self):
        self.assertEqual(Classifier.svm_classify(), 1)

    def test_good_1(self):
        self.assertEqual(Classifier.svm_classify(), 2)
    
    def test_good_2(self):
        self.assertEqual(Classifier.svm_classify(), 2)
    
    def test_good_3(self):
        self.assertEqual(Classifier.svm_classify(), 2)
    
    def test_strong_1(self):
        self.assertEqual(Classifier.svm_classify(), 3)

    def test_strong_2(self):
        self.assertEqual(Classifier.svm_classify(), 3)

    def test_strong_3(self):
        self.assertEqual(Classifier.svm_classify(), 3)

    def test_very_strong_1(self):
        self.assertEqual(Classifier.svm_classify(), 4)

    def test_very_strong_2(self):
        self.assertEqual(Classifier.svm_classify(), 4)

    def test_very_strong_3(self):
        self.assertEqual(Classifier.svm_classify(), 4)