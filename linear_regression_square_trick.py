from matplotlib import pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

w1_slope = -0.6
w2_intercept = 4
distance_from_y_intercept = -5
alpha  = 0.1
alphaq  = 0.01

xdata = np.arange(-15,15,0.5)
ydata = (w1_slope * xdata) + w2_intercept

#absolute trick adjustments
w1_absolute = w1_slope - (distance_from_y_intercept * alpha) 
w2_absolute = w2_intercept - alpha

y_absolute_trick = (w1_absolute * xdata) + (w2_absolute)

yvalue_at_q = ((w1_slope * distance_from_y_intercept) + w2_intercept)

q_minus_qapp = (3 - yvalue_at_q)
#square trick adjustments
w1_square = w1_slope - (distance_from_y_intercept * alphaq * -q_minus_qapp)
w2_square = (w2_intercept - (alphaq * -q_minus_qapp))

print(f'w1_square: {round(w1_square,2)} w2_square: {round(w2_square,2)} ' )

y_square_trick = (w1_square * xdata) + (w2_square)

plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.grid()
plt.plot([-5],[3], marker="o",markersize=5, markeredgecolor="red", markerfacecolor="green")
plt.plot(xdata,ydata)
plt.plot(xdata,y_absolute_trick)
plt.plot(xdata,y_square_trick)
plt.show()