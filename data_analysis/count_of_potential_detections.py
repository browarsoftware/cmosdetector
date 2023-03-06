import numpy as np
v01 = np.loadtxt('data/cropped/rp1.3.csv', delimiter=',')
v02 = np.loadtxt('data/cropped/rp2.0.csv', delimiter=',')

print(v01.shape[0])
for a in range(v01.shape[0]-2, -1, -1):
    v01[a] = v01[a] + v01[a+1]
v01 = v01.astype(int)

import matplotlib.pyplot as plt
plt.title("Count of potential detections below certain maximal pixel value v 1.3")
plt.plot(v01)
plt.axvline(x = 122, color = 'red', label = 'axvline - full height')
plt.axvline(x = 255, color = 'green', label = 'axvline - full height')
plt.xlabel("Threshold")
plt.ylabel("Count")
plt.show()


print(v02.shape[0])
for a in range(v02.shape[0]-2, -1, -1):
    v02[a] = v02[a] + v02[a+1]
v02 = v02.astype(int)

plt.title("Count of potential detections below certain maximal pixel value v 2.0")
plt.plot(v02)

plt.axvline(x = 180, color = 'red', label = 'axvline - full height')
plt.axvline(x = 255, color = 'green', label = 'axvline - full height')
plt.xlabel("Threshold")
plt.ylabel("Count")
plt.show()
