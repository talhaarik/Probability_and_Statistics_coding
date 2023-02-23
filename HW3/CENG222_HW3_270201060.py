import numpy as np
from matplotlib import pyplot as plt

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
### YOUR CODE HERE ###

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,normed=True)
hXa = plt.hist(Xa,100,alpha=0.5,normed=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.
### YOUR CODE HERE ###

# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,normed=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###