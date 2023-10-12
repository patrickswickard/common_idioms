import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# generate ten floats from zero to five, plot looks smooth but it's actually chunky
x_1 = np.linspace(0,5,10)
# y values are just squares of x values
y_1 = x_1**2
plt.plot(x_1,y_1)
plt.title('Numbers Squared Chart')
plt.xlabel('Numbers')
plt.ylabel('Numbers Squared')#
# if we were not in jupyter notebook we'd need plt.show() to show this plot
plt.show()
