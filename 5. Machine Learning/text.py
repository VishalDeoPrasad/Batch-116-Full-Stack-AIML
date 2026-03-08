import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
sales = [24000, 35000, 45000, 47000, 49000, 51000, 55000, 56000]

plt.plot(years,sales)
plt.title("years vs Sales");
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()