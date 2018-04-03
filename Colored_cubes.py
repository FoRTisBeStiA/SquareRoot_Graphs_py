import matplotlib.pyplot as plt

x_vals = list(range(1,5001))
y_vals = [x**3 for x in x_vals]
plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Reds, edgecolor='none', s=40)

plt.title("Cubed numbers", fontsize=24)
plt.xlabel("Cube Roots", fontsize=14)
plt.ylabel("Cube of Numbers", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.axis([0,5500,0,160000000000])
plt.show()
