"""
Compare the efficiency of class instantiation with and without
__slots__
"""

from random import randint
from timeit import timeit


ITERATIONS = int(1e6)


class Slotted:

    __slots__ = ('foo', 'bar')

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


class Regular:

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


global_slotted = Slotted('foo', 'bar')
global_regular = Regular('foo', 'bar')


def with_slots():
    c = Slotted(randint(0, 100), randint(0, 100))
    return c


def no_slots():
    c = Regular(randint(0, 100), randint(0, 100))
    return c


def slot_attr_access():
    return global_slotted.foo


def regular_attr_access():
    return global_slotted.foo


def slot_attr_assignment():
    global_slotted.foo = randint(0, 100)


def regular_attr_assignment():
    global_regular.foo = randint(0, 100)


to_test = (
    with_slots,
    no_slots,
    slot_attr_access,
    regular_attr_access,
    slot_attr_assignment,
    regular_attr_assignment
)


for func in to_test:
    time = timeit(func, number=ITERATIONS)
    print('{}:'.format(func.__name__))
    print('> total: ', time)
    print('> average: ', time / ITERATIONS)


'''
Results:

with_slots:
> total:  4.394950488000177
> average:  4.394950488000177e-06
no_slots:
> total:  4.8768404389848
> average:  4.8768404389848e-06
slot_attr_access:
> total:  0.14743318100227043
> average:  1.4743318100227043e-07
regular_attr_access:
> total:  0.14317270601168275
> average:  1.4317270601168275e-07
slot_attr_assignment:
> total:  2.0371140929928515
> average:  2.0371140929928516e-06
regular_attr_assignment:
> total:  2.0186321749933995
> average:  2.0186321749933995e-06
'''
