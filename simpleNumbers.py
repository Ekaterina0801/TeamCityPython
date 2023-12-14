import math
import random

def is_prime(num, test_count):
    for i in range(test_count):

        rnd = random.randint(1, num - 1)

        if (rnd ** (num - 1) % num != 1):
            return False

    return True

print (is_prime(12, 10)