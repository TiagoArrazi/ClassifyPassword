import string
import itertools


class Classifier:

    @classmethod
    def is_sequential(cls, pwd):
        seq = string.ascii_letters + string.digits
        positions = [seq.index(e) for e in pwd]

        for p in positions:
            pass

    @classmethod
    def is_consecutive(cls, pwd):
        consecs = [(char, len(list(group))) for char, group in itertools.groupby(pwd)]
        return max(each[1] for each in consecs)

    @classmethod
    def classify(cls, pwd):
        upper_case = set(list(string.ascii_uppercase))
        lower_case = set(list(string.ascii_lowercase))
        digits = set(list(string.digits))
        symbols = set(list(string.punctuation))

        set_pwd = set(list(pwd))
        features = list()
        penalties = list()

        if len(pwd) < 8:
            features.append(len(pwd) - 8)
            print("[FATAL] Password shorter than 8 characters")
            return 0

        if set_pwd.intersection(upper_case):
            features.append(len(pwd) - len(set_pwd.intersection(upper_case)))
        else:
            penalties.append("[WARNING] Missing upper case characters")

        if set_pwd.intersection(lower_case):
            features.append(len(pwd) - len(set_pwd.intersection(lower_case)))
        else:
            penalties.append("[WARNING] Missing lower case characters")

        if set_pwd.intersection(digits):
            features.append(len(pwd) - len(set_pwd.intersection(digits)))
        else:
            penalties.append("[WARNING] Missing digits")

        if set_pwd.intersection(symbols):
            features.append(len(pwd) - len(set_pwd.intersection(symbols)))
        else:
            penalties.append("[WARNING] Missing special characters")

        if cls.is_consecutive(pwd=pwd) >= 5:
            penalties.append("[WARNING] 5 or more consecutive characters were found")

        if cls.is_sequential(pwd=pwd):
            penalties.append("[WARNING] Sequential characters were found")

        [print(p) for p in penalties]

        if len(penalties) >= 2:
            print("[FATAL] 2 or more restrictions violated, password automatically acknowledged as WEAK")
            return 0

        elif len(pwd) - 2 <= sum(features) <= len(pwd) + 2:
            return 1

        elif 0 > sum(features) <= 15:
            return 0

        print("[SUCCEES] Violation threshold not reached")
        return 2


if __name__ == "__main__":
    while True:
        try:
            print(Classifier.is_sequential(input('Password: ')))

        except KeyboardInterrupt:
            exit(0)
