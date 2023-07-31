import matplotlib.pyplot as plt

data = {'Cetaphil (Inorganic)':83.2, 'Banana Boat (Organic)':80.0}
commercial = list(data.keys())
effectiveness = list(data.values())

fig = plt.figure(figsize = (7, 5))
plt.bar(commercial, effectiveness, color = 'maroon', width = 0.35)

c = [3.2, 13.4]
plt.errorbar(commercial, effectiveness, yerr=c, fmt="o", color = 'black')

plt.xlabel('Concentration (%)')
plt.ylabel('Average Amount of UV Blocked (mV)')
plt.title('The Effectiveness of Commercial Sunscreen')
plt.save()
