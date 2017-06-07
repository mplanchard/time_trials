"""
List.reverse() vs list[::-1]
"""

from timeit import timeit

repetitions = int(100000)


def method_one():
    lst = list(range(1000))
    return lst.reverse()

def method_two():
    lst = list(range(1000))
    return lst[::-1]


print('Method one:')
print(timeit(method_one, number=repetitions))
print('Method two:')
print(timeit(method_two, number=repetitions))


"""Results:
Method one:
2.036133544985205
Method two:
2.2113359259674326
"""

