import random

import Functions as F
import random


def even(no):
    if no % 2 == 0:
        return True
    else:
        return False


print(even(11))

no = [i for i in range(1, 11)]
r1 = res = filter(even, no)
print(*r1)
