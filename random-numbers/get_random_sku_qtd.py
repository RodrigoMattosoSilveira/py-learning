import sys
import Modules.my_random_calculators as r_calcs


a = float(sys.argv[1])
for i in range(100):
    items = r_calcs.get_random_poison(a)
    print(items)
