import numpy as np
import matplotlib.pyplot as plt
import random
import math

list_exp1_total = []
list_exp2_total = []
list_exp3_total = []
list_exp4_total = []
list_exp5_total = []

EXP_COUNT = 200000

def normal_pdf(x, mean, std):
    normal_dist_pdf = []
    for i in x:
        normal_dist_pdf.append((np.exp(-((((i-mean)/std)**2)/2)) / np.sqrt(np.pi*2))/std )
    return normal_dist_pdf
    # return (1 / (std * math.sqrt(2 * math.pi)) * math.exp(-1/2 * ((x-mean) *2 ) / std * 2))


def exp1():
    list_exp1 = []
    mean = (1/2) * 2
    std = math.sqrt((1/12) * 2)
    for i in range(EXP_COUNT):
        for k in range(2):
            j = random.uniform(0, 1)  # create 2 random numbers
            list_exp1.append(j)
            Sum = sum(list_exp1)
        list_exp1 = []  # empty the list, no backlog
        list_exp1_total.append(Sum)  # add totals to other list
        Sum = 0

    e1 = np.arange(mean-4*std, mean+4*std, 0.001)
    pdf = normal_pdf(e1, mean, np.std(list_exp1_total))
    plt.hist(list_exp1_total, bins=100, density=True, label="Histogram")
    plt.plot(e1, pdf, label="Normal distribution")
    plt.legend()
    plt.show()


def exp2():
    list_exp2 = []
    mean = (1 / 2) * 4
    std = (1 / 12) * 4
    for i in range(EXP_COUNT):
        for k in range(4):
            j = random.uniform(0, 1)  # create 4 random numbers
            list_exp2.append(j)
            Sum = sum(list_exp2)
        list_exp2 = []  # empty the list, no backlog
        list_exp2_total.append(Sum)  # add totals to other list
        Sum = 0

    e2 = np.arange(mean - 4*std, mean + 4*std, 0.001)
    pdf = normal_pdf(e2, mean, np.std(list_exp2_total))
    plt.hist(list_exp2_total, bins=100, density=True, label="Histogram")
    plt.plot(e2, pdf, label="Normal distribution")
    plt.legend()
    plt.show()


def exp3():
    list_exp3 = []
    mean = (1 / 2) * 50
    std = math.sqrt((1 / 12) * 50)
    for i in range(EXP_COUNT):
        for k in range(50):
            j = random.uniform(0, 1)  # create 50 random numbers
            list_exp3.append(j)
            Sum = sum(list_exp3)
        list_exp3 = []  # empty the list, no backlog
        list_exp3_total.append(Sum)  # add totals to other list
        Sum = 0


    e3 = np.arange(mean - 4 * std, mean + 4 * std, 0.001)
    pdf = normal_pdf(e3, mean, np.std(list_exp3_total))
    plt.hist(list_exp3_total, bins=100, density=True, label="Histogram")
    plt.plot(e3, pdf, label="Normal distribution")
    plt.legend()
    plt.show()


def exp4():
    list_exp4 = []
    for i in range(EXP_COUNT):
        for j in range(50):
            if j == 0:
                k = random.uniform(0, 200)
                list_exp4.append(k)
                Sum = sum(list_exp4)
            else:
                if list_exp4[-1] < 99:
                    k = random.uniform(0, 200)
                    list_exp4.append(k)
                    Sum = sum(list_exp4)
                else:
                    k = random.uniform(98, 102)
                    list_exp4.append(k)
                    Sum = sum(list_exp4)
        list_exp4 = []
        list_exp4_total.append(Sum)
        Sum = 0

    mean = np.mean(list_exp4_total)
    std = np.std(list_exp4_total)
    e4 = np.arange(mean - 4*std, mean + 4*std, 0.001)
    pdf = normal_pdf(e4, mean, std)
    plt.hist(list_exp4_total, bins=100, density=True, label="Histogram")
    plt.plot(e4, pdf, label="Normal distribution")
    plt.legend()
    plt.show()


def exp5():
    list_exp5 = []
    for i in range(EXP_COUNT):
        for j in range(50):
            a = random.uniform(0, 1)
            b = random.uniform(0, 1)
            k = random.uniform(min(a, b), (max(a, b)))
            list_exp5.append(k)
            Sum = sum(list_exp5)
        list_exp5 = []
        list_exp5_total.append(Sum)
        Sum = 0

    mean = np.mean(list_exp5_total)
    std = np.std(list_exp5_total)
    e5 = np.arange(mean - 4*std, mean + 4*std, 0.001)
    pdf = normal_pdf(e5, mean, std)
    plt.hist(list_exp5_total, bins=100, density=True, label="Histogram")
    plt.plot(e5, pdf, label="Normal distribution")
    plt.legend()
    plt.show()


exp1()
exp2()
exp3()
exp4()
exp5()