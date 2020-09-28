import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib.ticker import MaxNLocator

apl_price = [93.95, 112.15, 104.05, 144.85, 169.49]
ms_price = [19.01, 50.29, 57.05, 69.98, 94.39]
year = [2014, 2015, 2016, 2017, 2018]

plt.plot(year, apl_price, 'ok',
        year,ms_price, 'g')

plt.xlabel('Year')
plt.ylabel('Stock Price')

plt.show()

fig_1 = plt.figure(1, figsize=(20, 5))

apple_price = fig_1.add_subplot(121)
microsoft_price = fig_1.add_subplot(122)

apple_price.plot(year, apl_price)
apple_price.xaxis.set_major_locator(MaxNLocator(integer=True))

microsoft_price.scatter(year, ms_price)
microsoft_price.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()

fig_2, axes = plt.subplots(2,2,figsize=(20, 5))
axes[0,1].scatter(year, apl_price)
axes[1,0].plot(year, ms_price)
plt.show()