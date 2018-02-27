#import random
#def random_item(iterable):
#    secret_num = random.randint(0,(len(iterable)-1))
#    print(secret_num)
#    print(iterable[secret_num])
#    return iterable[secret_num]
#
#random_item("sasquatch")

import random

start = 5

def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2

while start != False:
    potato = random.randint(1, 99)
    if even_odd(potato):
        print("{} is even".format(potato))
    else:
        print("{} is odd".format(potato))
    start -= 1