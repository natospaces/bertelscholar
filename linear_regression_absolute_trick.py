from matplotlib import pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

w1_slope = -0.6
w2_intercept = 4
distance_from_y_intercept = -5
alpha  = 0.1

xdata = np.arange(-10,10,0.5)
ydata = (w1_slope * xdata) + w2_intercept

w1 = w1_slope - (distance_from_y_intercept * alpha)
w2 = w2_intercept - alpha

print(f'w1: {round(w1,1)} w2: {w2} ' )
ydata2 = (w1 * xdata) + (w2)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
plt.plot([-5],[3], marker="o",markersize=5, markeredgecolor="red", markerfacecolor="green")
plt.plot(xdata,ydata)
plt.plot(xdata,ydata2)
plt.show()