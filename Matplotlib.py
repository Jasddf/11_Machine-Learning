import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,13,18,20]

plt.plot(x,y, marker='*', linestyle='--', color='red', label='temp')
plt.title('Daily temperature trend')
plt.xlabel('Time(Hour)')
plt.ylabel('Temperature(C)')
plt.legend()
plt.grid(True)
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.style.use('_mpl-gallery-nogrid')
#
# # make data: correlated + noise
# np.random.seed(1)
# x = np.random.randn(5000)
# y = 1.2 * x + np.random.randn(5000) / 3
#
# # plot:
# fig, ax = plt.subplots()
#
# ax.hist2d(x, y, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))
#
# ax.set(xlim=(-2, 2), ylim=(-3, 3))
#
# plt.show()