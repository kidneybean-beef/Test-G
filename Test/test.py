#******************************************************************************
#ProjectName:    Introduction to Finite Element Methods 
#LastModifiedBy: A.Winterstein@tum.de
#Date:           Oct2017
#Revision:       1.0
#******************************************************************************

#This small programm checks if your installation of Pyhton3 is correct.

import numpy as np
import matplotlib.pyplot as plt
import math


n_values = 50
x = np.zeros(n_values+1)
i = 0
n = 0

while (i <= n_values):
    x[i] = math.cos(n * math.pi)
    i= i + 1
    n = n + 0.1
    
plt.plot(x)
plt.show()

#I add some...
