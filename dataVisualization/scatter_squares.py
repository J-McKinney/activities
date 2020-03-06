import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# colormap is a series of colors in a gradient that moves from start to finish
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# use c to represent a color
# ax.scatter(x_values, y_values, c='red', s=10)
# you can also use RGB colors too
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Set chart title and label axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for x axis
ax.axis([0, 1100, 0, 1100000])

plt.show()

# saves the graph that plt.show() gives us as a png image in our file/directory
# plt.savefig('squares_plot.png', bbox_inches='tight')