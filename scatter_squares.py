import matplotlib.pyplot as plt

x_vals = list(range(1,1001))
y_vals = [x**2 for x in x_vals]
plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Set Chart Title and Label Axes.
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of Tick Labels.
#plt.tick_params(axis='both', which='major', labelsize=14)

# Set range for ech axis.
plt.axis([0,5001,0,110000])

plt.show()
