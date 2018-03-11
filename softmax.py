import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    lexp = np.exp(L)
    sumexp = np.sum(lexp)
    result = []
    for i in lexp:
       result.append((i*1.0)/sumexp)
    return result
     
