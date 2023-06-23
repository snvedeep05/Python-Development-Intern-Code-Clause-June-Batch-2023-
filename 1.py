import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [2, 4, 6, 8, 10]

plt.stackplot(x, y1, y2, labels=['Variable 1', 'Variable 2'])
plt.legend(loc='upper left')
plt.show()
