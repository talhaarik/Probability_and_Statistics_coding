#  Talha Arık - 270201060
import numpy as np
import math
from matplotlib import pyplot as plt

# PART A ---------------------------------------------------------------------------------------------------

Sample_set = {0.3, 0.6, 0.8, 0.9}
Sample_list = list(Sample_set)  # I find it easier to use a list.


def fx_function(x, Q):
    return (2 * Q ** 2) / x ** 3  # f(x) function


def method_of_moments_function(sample):
    return np.mean(sample) / 2


def maximum_likelihood_estimation(sample):
    return min(sample)  # When it becomes zero, it reaches its maximum value. 0.3 chosen because 0.3 is closer to 0
    # than 0.9


print("MoM estimate for the sample is:", method_of_moments_function(Sample_list))
print("MLE estimate for the sample is:", maximum_likelihood_estimation(Sample_list))

# PART B ---------------------------------------------------------------------------------------------------
U = []  # Random variables
p = []  # Population array


def inverse_transformation_method_func(Q, u):
    return np.sqrt(np.square(Q) / (1 - u))


def inverse_transformation_method():
    for i in range(10000000):
        u = np.random.rand()
        x = inverse_transformation_method_func(2.4, u)
        U.append(u)
        p.append(x)


# PART C ---------------------------------------------------------------------------------------------------
inverse_transformation_method()

N = [1, 2, 3, 4, 5, 10, 50, 100, 500, 1000]
method_of_moments_estimates_list = []
maximum_likelihood_estimates_list = []


def part_c(p, n):
    outer_list = []
    for a in range(100000):
        inner_list = []
        for j in range(n):
            inner_list.append(p[np.random.randint(0, 10000000)])
        outer_list.append(inner_list)

    for a in outer_list:
        method_of_moments_estimates_list.append(method_of_moments_function(a))
        maximum_likelihood_estimates_list.append(maximum_likelihood_estimation(a))

    bins = np.linspace(0, 4.8, 100)
    plt.hist(method_of_moments_estimates_list, bins, density=True, alpha=0.5, label="MoM Estimation for N" + str(n))
    plt.hist(maximum_likelihood_estimates_list, bins, density=True, alpha=0.5, label="Mle Estimation for N" + str(n))
    plt.show()

    print("For N=", n)
    print("MoM estimate mean:", np.mean(method_of_moments_estimates_list))
    print("MLE estimate mean:", np.mean(maximum_likelihood_estimates_list))
    print("MoM estimate std:", np.std(method_of_moments_estimates_list))
    print("MLE estimate std:", np.std(maximum_likelihood_estimates_list))


for b in N:
    part_c(p, b)

