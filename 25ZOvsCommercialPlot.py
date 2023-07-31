import matplotlib.pyplot as plt
data = {'25% ZO':70.7, 'Cetaphil (Inorganic)':83.2,
        'Banana Boat (Organic)':80.0}
sunscreenType = list(data.keys())
effectiveness = list(data.values())

fig = plt.figure(figsize = (9, 5))
plt.bar(sunscreenType, effectiveness, color = 'maroon', width = 0.35)
c = [9.0, 3.2, 13.4]

plt.errorbar(sunscreenType, effectiveness, yerr=c, fmt = "o", color = 'black')

plt.xlabel('Type of Sunscreen')
plt.ylabel('Average amount of UV Blocked (%)')
plt.title('25% Zinc Oxide vs. Commercial')
plt.show()
