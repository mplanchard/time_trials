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


def time_with_slots():
    c = Slotted(randint(0, 100), randint(0, 100))
    return c


def time_no_slots():
    c = Regular(randint(0, 100), randint(0, 100))
    return c


def time_slot_attr_access():
    return global_slotted.foo


def time_regular_attr_access():
    return global_slotted.foo


def time_slot_attr_assignment():
    global_slotted.foo = randint(0, 100)


def time_regular_attr_assignment():
    global_regular.foo = randint(0, 100)


def time_slot_attr_lookup():
    return hasattr(global_slotted, 'foo')


def time_regular_attr_lookup():
    return hasattr(global_regular, 'foo')


to_test = (v for k, v in dict(locals()).items() if k.startswith('time_'))


for func in to_test:
    time = timeit(func, number=ITERATIONS)
    print('{}:'.format(func.__name__.replace('time_', '')))
    print('> total: ', time)
    print('> average: ', time / ITERATIONS)
    print()


'''
Results:

regular_attr_assignment:
> total:  2.013330613990547
> average:  2.0133306139905473e-06

slot_attr_access:
> total:  0.14955477498006076
> average:  1.4955477498006076e-07

slot_attr_assignment:
> total:  2.08173781100777
> average:  2.0817378110077698e-06

regular_attr_access:
> total:  0.14511376500013284
> average:  1.4511376500013283e-07

with_slots:
> total:  4.468222044000868
> average:  4.468222044000868e-06

no_slots:
> total:  5.064206484996248
> average:  5.064206484996248e-06

slot_attr_lookup:
> total:  0.22497813901281916
> average:  2.2497813901281915e-07

regular_attr_lookup:
> total:  0.2263577709964011
> average:  2.2635777099640107e-07
'''
