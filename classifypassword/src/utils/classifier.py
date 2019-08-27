import string
import itertools


class Classifier:

    @classmethod
    def seq_char(cls, password):

        seq = list()

        chars = string.ascii_lowercase
        digits = string.digits

        for i, c in enumerate(password):
            if c in chars:
                pos_in_chars = chars.index(c)

            elif c in digits:

            else:
                pass



    @classmethod
    def svm_classify(cls, password):

        weights = list()
        length = len(password) * 4
        lower_case = (len(password) - sum(1 for c in password if c.islower())) * 2
        upper_case = (len(password) - sum(1 for c in password if c.isupper())) * 2
        digits = sum(1 for c in password if c.isdigit()) * 4
        symbols = sum(1 for c in password if c in string.punctuation) * 6
        middle_num_sym = sum(1 for i, c in enumerate(password) if c.isdigit() or c in string.punctuation
                             and i != -1 and i != 0)

        if digits == 0 and symbols == 0:
            char_only = len(password) * -1
        else:
            char_only = 0

        if lower_case == 0 and upper_case == 0 and symbols == 0:
            digits_only = len(password) * -1
        else:
            digits_only = 0

        tmp_repeat = len(set(list(password)))
        if tmp_repeat > len(password):
            repeated_char = -tmp_repeat * (tmp_repeat - 1)
        else:
            repeated_char = 0

        group = itertools.groupby(password)
        consec_chars = sum([-n * 2 for n in [len(label * sum(1 for _ in g)) for label, g in group]])


