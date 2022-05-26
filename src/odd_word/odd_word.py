# -*- coding: utf-8 -*-
"""
    It returns a string of a given length
    the way that each letter occurs an odd number of times
"""


import random
import string
import sys
import re


def odd_word(number):
    '''
        It returns a string of a given length
        the way that each letter occurs an odd number of times
    '''

    if not number.isdigit():
        return 'Nothing to return, wrong input. It must be an integer'

    number = int(number)

    assert isinstance(number, int), 'Nothing to return, wrong input. It must be an integer'
    assert  number > 0, 'Nothing to return, wrong input. It must be greater than 0'

    alphabet = string.ascii_lowercase
    output = ''

    while len(output) != number:
        random_str = ''
        num = number - len(output)
        if not num:
            break

        while num > 0:
            random_idx = random.randrange(0, len(alphabet))
            random_str += alphabet[random_idx]
            num = num - 1

        letter_counter = dict([(k[0], 0) for k in random_str])

        for l_c in random_str:
            letter_counter.update({l_c: letter_counter[l_c] + 1})

        odd_letters = ''
        for k_l, v_l in letter_counter.items():
            if v_l % 2 > 0:
                odd_letters += k_l

        pattern = re.compile("[%s]" % odd_letters)
        result = pattern.findall(random_str)
        result = ''.join(result)
        output += result

    return output


if __name__ == '__main__':
    if len(sys.argv) == 2:
        COUNT = sys.argv[1]
    else:
        COUNT = '4'
    print(odd_word(COUNT))
