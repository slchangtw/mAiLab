#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import time

# 1. generate an array of 5 random values
np.random.seed(1)
print(np.random.randn(5))

# [ 1.62434536 -0.61175641 -0.52817175 -1.07296862  0.86540763]

# 2. generate N random numbers between -1 and 1, N are 10^1, 10^2, 10^3, 10^4, and 10^5
# Besides, print the mean and standard deviation of those random numbers
def gen_randm_numbers(n):
    np.random.seed(1)
    randn_array = np.random.uniform(-1, 1, 10**n)
    print("Mean: {:.4f}".format(np.mean(randn_array)))
    print("Standard Deviation: {:.4f}".format(np.std(randn_array)))

for n in range(1, 6):
    # 3. print elapsed time
    t = time.process_time()
    print("Generate {} random values:".format(10**n))
    gen_randm_numbers(n)
    elapsed_time = time.process_time() - t
    print("Elapsed Time:{:.7f}\n".format(elapsed_time))
# Generate 10 random values:
# Mean: -0.3707
# Standard Deviation: 0.4129
# Elapsed Time:0.0014050

# Generate 100 random values:
# Mean: -0.0282
# Standard Deviation: 0.5888
# Elapsed Time:0.0017930

# Generate 1000 random values:
# Mean: 0.0012
# Standard Deviation: 0.5767
# Elapsed Time:0.0014970

# Generate 10000 random values:
# Mean: -0.0040
# Standard Deviation: 0.5754
# Elapsed Time:0.0010310

# Generate 100000 random values:
# Mean: -0.0016
# Standard Deviation: 0.5787
# Elapsed Time:0.0029850

# 4. implement a random number generator using linear congruential generator algorithm
# an arguable drawback of the implementation is that one must set the random seed when using the function  
def lcg(num, seed=None):
    if seed is not None:
        pre_rnumber = seed
    for i in range(num):
        # recurrence relation: Xn+1 = (Xn * a + c) mod m
        rnumber = (pre_rnumber * 1103515245 + 12345) % (2**31)
        yield rnumber
        pre_rnumber = rnumber

print(list(lcg(num = 5, seed=10)))
# [297746555, 1849040536, 736986865, 581309142, 1106733399]