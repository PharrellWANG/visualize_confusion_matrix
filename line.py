import matplotlib.pyplot as plt

x_axis = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y_axis = [0.650, 0.711, 0.759, 0.795, 0.823, 0.846, 0.867, 0.884,
          0.897, 0.909, 0.919, 0.929, 0.936, 0.944, 0.950, 0.955]

x1_axis = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y1_axis = [0.801, 0.842, 0.873, 0.895, 0.912, 0.924, 0.934, 0.942,
           0.949, 0.955, 0.961, 0.965, 0.970, 0.974, 0.977, 0.980]

x2_axis = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y2_axis = [0.819, 0.860, 0.891, 0.912, 0.927, 0.938, 0.947, 0.955,
           0.961, 0.966, 0.970, 0.973, 0.977, 0.980, 0.983, 0.985]

# 1 & Top-5 & 0.651 \\

plt.plot(x_axis, y_axis)
plt.plot(x1_axis, y1_axis)
plt.plot(x2_axis, y2_axis)
# plt.title('Top-k precision on validation datasets for blocks of size 8x8, 16x16 and 32x32')
plt.xlabel('Value of k')
plt.ylabel('Precision')

plt.legend(['8x8', '16x16', '32x32'], loc='upper left')

plt.axis([5, 20, 0.6, 1])
plt.savefig('figures/xxx.pdf', format='pdf', dpi=1200)
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(10)
#
# plt.plot(x, x)
# plt.plot(x, 2 * x)
# plt.plot(x, 3 * x)
# plt.plot(x, 4 * x)
#
# plt.legend(['y = x', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
#
# plt.show()