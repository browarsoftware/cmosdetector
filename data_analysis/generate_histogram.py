import glob
import cv2
import numpy as np
def generate_data(path):
    my_files = glob.glob(path)
    val = []
    for my_file in my_files:
        img = cv2.imread(my_file)
        img2 = np.zeros((img.shape[0], img.shape[1]))
        #img2 = img[:, :, 0] + img[:, :, 1] + img[:, :, 2]
        img2 = img2 + img[:, :, 0]
        img2 = img2 + img[:, :, 1]
        img2 = img2 + img[:, :, 2]

        max_val = np.max(img2)
        val.append(max_val)
    return val

val1 = generate_data(path = "data\\cropped\\rp13\\*.png")
val2 = generate_data(path = "data\\cropped\\rp20\\*.png")

import matplotlib.pyplot as plt
import seaborn as sns
counts1, bins1 = np.histogram(val1)

counts2, bins2 = np.histogram(val2)

plt.title("Density plot of highest pixel value")

plt.xlim([255, 765])
plt.xlabel("Highest pixel value")

print(len(val1))
print(len(val2))


sns.distplot(val1, hist=True, kde=False,
             bins=int(20), color = 'red',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4, 'color': 'orange'}
             )

sns.distplot(val2, hist=True, kde=False,
             bins=int(20), color = 'green',
             hist_kws={'edgecolor':'black'},
             #kde_kws={'linewidth': 4, 'color': 'cyan'}
             )
plt.show()


plt.title("Histogram of highest pixel value")
plt.stairs(counts1, bins1, color='red')
plt.stairs(counts2, bins2, color='green')
plt.ylabel("Count")
plt.show()

