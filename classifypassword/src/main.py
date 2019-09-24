from src.utils.classifier import Classifier


if __name__ == '__main__':
    print(Classifier.__doc__)
    print(Classifier.classify(input('Password: ')))