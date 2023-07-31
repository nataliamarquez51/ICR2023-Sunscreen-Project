import matplotlib.pyplot as plt

a = [0, 5, 10, 12, 15, 20, 25, 50]
b = [8.8, 22.3, 45.7, 32.3, 51.0, 52.9, 70.7, 80.8]
plt.scatter(a, b)

c = [1.1, 7.3, 5.8, 12.9, 5.7, 6.2, 9.0, 6.9]

plt.errorbar(a, b, yerr=c, fmt="o", color = 'black')

plt.xlabel('Concentration (%)')
plt.ylabel('Average Amount of UV Blocked (%)')
plt.title('The Effect of Concentration on Effectiveness')
plt.show()
