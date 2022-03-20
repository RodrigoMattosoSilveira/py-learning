import numpy as np
import random
from math import trunc

a, m = 1., 1.160964  # shape and mode
for i in range(0, 100):
    s = (np.random.pareto(a, 1000) + 1) * m
    j = random.randint(1, 100)
    # print (s)
    randomNumber = trunc(s[j] + 0.5)
    orderItems = randomNumber
    if orderItems > 12:
        orderItems = 12
    else:
        if 3 < orderItems < 12:
            orderItems = 6
        else:
            orderItems = 1

    print('Number %s orderItems %s' % (randomNumber, orderItems))
