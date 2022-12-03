#  A program to make use of MatPlotLib to display a graph
#  Author:  Kimberley Snow

import matplotlib.pyplot as plt

x_axis = []
y_axis = []

for x in range(0, 12):
    x = input("Please enter the Month (as Jan, Feb, Mar, etc):  ")
    y = input("Please enter the Monthly Claim Amount for each month:  ")
    x_axis.append(x)
    y_axis.append(y)

plt.plot(x_axis, y_axis, color='purple', marker="D")

#learned I cannot add values to a legend, unless they are a str.
#Total = sum(y_axis)
#plt.legend("YEARLY TOTAL =", Total)

plt.xlabel("Month")
plt.ylabel("Monthly Claim Amount (Dollars)")

plt.title("Revenue Report ")
plt.grid(True)

plt.show()


