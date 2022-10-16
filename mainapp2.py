import matplotlib.pyplot as plt
import numpy as np


def coefficients_calculation(x_values, y_values):
    average_x = 0
    average_y = 0
    average_xy = 0
    average_xx = 0
    n = len(x_values)
    for i in range(n):
        average_x += x_values[i]
        average_y += y_values[i]
        average_xy += x_values[i]*y_values[i]
        average_xx += x_values[i]**2
    average_x = average_x/n
    average_y = average_y/n
    average_xy = average_xy/n
    average_xx = average_xx/n
    d_x = average_xx - average_x**2
    a = (average_xy - average_x*average_y)/d_x
    b = average_y - a * average_x
    return (a, b)


x = np.linspace(0,2*3.14,25)
y = np.sin(x)



plt.scatter(x,y);
a = coefficients_calculation(x, y)
y1 = [a[0]*i+a[1] for i in x]
y1 = np.array(y1)

print(np.mean(y1**2-y**2))
plt.plot(x,y1)
plt.show()

# http://www.cleverstudents.ru/articles/mnk.html
