import sys
import Modules.my_random_calculators as r_calcs

# a = float(sys.argv[1])
arr = [0, 1]
freq = [25, 75]
n = len(arr)
for i in range(10):
    item = r_calcs.rng_apd(arr, freq, n)
    print(item)
