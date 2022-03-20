import sys
import Modules.my_random_calculators as mrn

# mu = 10, sigma = 2.6
mu = float(sys.argv[1])
sigma = float(sys.argv[2])

for i in range(0, 10):
    m = mrn.get_random_normal(mu, sigma)
    print(m)

