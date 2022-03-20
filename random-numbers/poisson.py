import numpy as np
import random


for i in range(0, 10):
    s = np.random.poisson(10, 100)
    j = random.randint(1, 100)
    # print (s)
    print(s[j])
