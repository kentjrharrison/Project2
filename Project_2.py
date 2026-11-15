import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
data = np.loadtxt("data.csv", delimiter=",", dtype=str)
print(data)
x = data[1:, 0].astype(np.float32)
y= data[1:, 1].astype(np.float32)
print("y = ", y)
print("x = ", x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
### EXERCISE 1
x_units='gram'
y_units='milimeters'
print_equation(slope,intercept,y_units,x_units)
### EXERCISE 2
fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("mass (g)") #change the units as appropriate
plt.ylabel("distance in y direction (millimeters)")  #change the units as appropriate
plt.show()
fig.savefig('dataplot.png')
