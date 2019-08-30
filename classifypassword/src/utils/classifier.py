import string
import itertools


class Classifier:

    @classmethod
    def seq_char(cls, password):

        sequences = list()

        chars = string.ascii_lowercase
        digits = string.digits

        for i, c in enumerate(password):
            if c.lower() in chars:
                acc = 0
                pos_in_chars = chars.index(c.lower())
                for d in password[i:]:


            elif c in digits:
                pos_in_digits = digits.index(c)

            else:
                pass

    @classmethod
    def svm_classify(cls, password):

        weights = list()
        weights.append(len(password) * 4) # password length
        weights.append((len(password) - sum(1 for c in password if c.islower())) * 2) # lower case characters
        weights.append((len(password) - sum(1 for c in password if c.isupper())) * 2) # upper case characters

        digits = sum(1 for c in password if c.isdigit()) * 4
        weights.append(digits) # digits

        weights.append(sum(1 for c in password if c in string.punctuation) * 6) # symbols
        weights.append(sum(1 for i, c in enumerate(password) if c.isdigit() or c in string.punctuation
                             and i != -1 and i != 0)) # digits & symbols in the middle



        if digits == 0 and symbols == 0: # characters only
            char_only = len(password) * -1
        else:
            char_only = 0

        if lower_case == 0 and upper_case == 0 and symbols == 0: # digits only
            digits_only = len(password) * -1
        else:
            digits_only = 0

        tmp_repeat = len(set(list(password))) # repeated characters
        if tmp_repeat > len(password):
            repeated_char = -tmp_repeat * (tmp_repeat - 1)
        else:
            repeated_char = 0

        group = itertools.groupby(password) # consecutive characters
        consec_chars = sum([-n * 2 for n in [len(label * sum(1 for _ in g)) for label, g in group]])


