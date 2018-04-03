import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
square = [1,4,9,16,25]
plt.plot(input_values, square, linewidth=5)

# Set Chart Title and Label Axes.
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of Tick Labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
