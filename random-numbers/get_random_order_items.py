import sys
import Modules.my_random_calculators as rcals


def get_random_order_items(_mu, _sigma):
    new_order_items = rcals.get_random_pareto(_mu, _sigma)
    if new_order_items > 12:
        new_order_items = 12
    else:
        if 3 < new_order_items < 12:
            new_order_items = 6
        else:
            new_order_items = 1
    return new_order_items

# orders 1, 1.160964
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# print('mu:', sys.argv[1])
# print('sigma:', sys.argv[2])
mu = float(sys.argv[1])
sigma = float(sys.argv[2])
# print('mu:', mu)
# print('sigma:', sigma)

for i in range(100):
    print(get_random_order_items(mu, sigma))
