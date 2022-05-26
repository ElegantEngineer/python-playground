# -*- coding: utf-8 -*-
"""
    It returns count of the minimum number of letters
    that could be deleted from a given string to create
    a new one in which every letter occurs a unique number of times
"""


import sys


def distinct_letters_match_count(sequence):
    '''
        It returns count of the minimum number of letters
        that could be deleted from a given string to create
        a new one in which every letter occurs a unique number of times
    '''

    letter_counter = dict([(k[0], 0) for k in sequence])
    cnt = 0
    queue = list()

    for l_c in sequence:
        letter_counter.update({l_c: letter_counter[l_c] + 1})

    for k in letter_counter:
        queue.append(letter_counter[k])

    queue = sorted(queue)

    while len(queue) > 0:
        frequent = queue.pop()

        if len(queue) == 0:
            return cnt

        if frequent == queue[-1]:
            if frequent > 1:
                queue.append(frequent - 1)
            cnt += 1
        queue = sorted(queue)

    return cnt


if __name__ == '__main__':
    if len(sys.argv) == 2:
        WORD = sys.argv[1]
    else:
        WORD = 'aabb'
    print(distinct_letters_match_count(WORD))
