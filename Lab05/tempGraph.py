# Author: Michael Savino
# Date: 10/3/24
# Description: A program to generate temperatures in 3 different cities, then plot them against time

import matplotlib.pyplot as plt
import random
time = [1,2,3,4,5,6,7,8,9,10,11,12]

newyorkCity = []
losAngeles = []
charleston = []

cities = [newyorkCity,losAngeles,charleston]

for i in range(len(cities)):
    for j in range(12):
        cities[i].append(random.randint(10,30))

plt.title("Hourly Temperatures")

plt.xlabel("Hours")
plt.ylabel("Temperature")

plt.plot(time, newyorkCity, label="NYC")
plt.plot(time, losAngeles, label="Los Angeles")
plt.plot(time, charleston, label="Charleston")


plt.legend(["NYC", "Los Angeles", "Charleston"])

plt.show()
