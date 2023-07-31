import matplotlib.pyplot as plt

data = {'Plastic Only':7.8, '0% ZO':8.8, '5% ZO':22.3, '10% ZO':45.7,
        '12% ZO':32.2, '15% ZO':51.0, '20% ZO':52.9, '25% ZO':70.7,
        '50% ZO':80.8, 'Cetaphil':83.2,
        'Banana Boat':80.0}
sunscreenType = list(data.keys())
effectiveness = list(data.values())

fig = plt.figure(figsize = (12, 5))
plt.bar(sunscreenType, effectiveness, color = 'maroon', width = 0.35)
c = [0.7, 1.1, 7.3, 5.8, 12.9, 5.7, 6.2, 9.0, 6.9, 3.2, 13.4]

plt.errorbar(sunscreenType, effectiveness, yerr=c, fmt="o", color = 'black')

plt.xlabel('Type of Sunscreen')
plt.ylabel('Average Amount of UV Blocked (%)')
plt.title('Homemade vs. Commercial')
plt.savefig('SunscreenDataPlot.png')
