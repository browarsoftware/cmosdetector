import glob
import cv2

def generate_data(path):
    my_files = glob.glob(path)
    val = []
    for a in range(len(my_files)):

        my_file = my_files[a]
        img = cv2.imread(my_file)

        img2 = np.zeros((img.shape[0], img.shape[1]))
        img2 = img2 + img[:, :, 0]
        img2 = img2 + img[:, :, 1]
        img2 = img2 + img[:, :, 2]

        idx = (0,0)
        mm = np.max(img2)
        if mm > 0:
            for a in range(img2.shape[0]):
                for b in range(img2.shape[1]):
                    if img2[a,b] == mm:
                        idx = (a, b)
                        val.append(idx)

    return val

val1 = generate_data(path = "d:\\path_to_raw_data\\*.png")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.ndimage.filters import gaussian_filter


def myplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    heatmap[0:50,0:50] = 0
    heatmap[950:1000, 0:50] = 0
    heatmap[0:50, 950:1000] = 0
    heatmap[950:1000, 950:1000] = 0

    return heatmap.T, extent

fig, axs = plt.subplots(1, 1)

s = 4
x = []
y = []
for zz in val1:
    x.append((zz[0]))
    y.append((zz[1]))

y.append(0)
x.append(0)

y.append(1920)
x.append(0)

y.append(1920)
x.append(1080)

y.append(0)
x.append(1080)

x = np.array(x)
y = np.array(y)
img, extent = myplot(y, x, s)


plt.xlabel("X [pixels]")
plt.ylabel("Y [pixels]")
axs.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
axs.set_title("Distribution of hits on camera v.2.0 (Gaussian smoothing with  $\sigma$ = %d)" % s)
plt.show()
