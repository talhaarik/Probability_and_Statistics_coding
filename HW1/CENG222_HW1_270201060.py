# Talha Arık HW-1/270201060

import matplotlib.pyplot as plt
import random
import numpy as np

non_three = 5/6
sample_space = 1
rolling_die = 5

N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]


def at_least_givenOneThree_andOneEven_situation():
    non_even =  (1/2)**rolling_die
    at_least_one_even = (sample_space - non_even)
    nonThree_nonEven = (1/3)**rolling_die
    atLeastOneThree_atLeastOneEven = (sample_space - nonThree_nonEven)
    nonThree_intersection_nonEven = at_least_one_three_situation() + at_least_one_even - atLeastOneThree_atLeastOneEven
    outcome = nonThree_intersection_nonEven / at_least_one_even
    return outcome 

def at_least_one_three_situation():
    non_three_ofAll = (non_three**rolling_die)
    result = sample_space - non_three_ofAll
    return result

def atLeastOneThree_and_onlyOneEven():
    return 0

def roll_n_dice(die_number, die_type):
    die_low_limit = 1
    die_up_limit = die_type
    die = list()
    for a in range(die_number):
        die.append(np.random.randint(die_low_limit, die_up_limit+1))
    return die

def are_there_one_even_die(die_list):
    for a in die_list:
        if a%2 == 0:
            return True
    return False

def are_there_only_one_even(die_list):
    sum = 0
    for a in die_list:
        sum += (a%2)
    if sum == 4: 
        return True
    return False       

def p1_experiment():
    outcomes = list()
    counter = 0
    for b in N:
        for a in range(b):
            dice = roll_n_dice(5, 6)
            if 3 in dice:
                counter += 1
        outcome = counter / b
        outcomes.append(outcome)
        counter = 0     
    return outcomes

def p3_experiment():
    outcomes = list()
    counter = 0
    for a in N:
        for b in range(a):
            die = roll_n_dice(5, 6)
            while(not are_there_only_one_even(die)):
                die = roll_n_dice(5, 6)     
            if not 3 in die:
                continue
            counter += 1
        outcome = counter / a
        outcomes.append(outcome)
        counter = 0
    return outcomes

def p2_experiment():
    outcomes = list()
    counter = 0
    for a in N:
        for b in range(a):
            die = roll_n_dice(5, 6)
            while(not are_there_one_even_die(die)):
                die = roll_n_dice(5, 6)  
            if not 3 in die:
                continue
            counter += 1
        outcome = counter / a    
        outcomes.append(outcome)
        counter = 0
    return outcomes 

result1 = p1_experiment()
result_1 = at_least_one_three_situation()
result2 = p2_experiment()
result_2 = at_least_givenOneThree_andOneEven_situation()
result3 = p3_experiment()
print(result1)
print(result2)
print(result3)

plt.axhline(result_1, label = 'Theoretical result of P1', linestyle='-', color = 'r')
plt.axhline(result_2, label = 'Theoretical result of P2', linestyle = '-', color = 'b')
plt.plot(N, result1, label='Experiment 1', color= 'b')
plt.plot(0, result_1, label = 'Theoretical result of P1')
plt.plot(N, result2, label='Experiment 2')
plt.plot(N, result3, label='Experiment 3')
plt.xscale("log")
plt.xlabel("Experiment Count")
plt.ylabel("Result")
plt.legend()
plt.show()

