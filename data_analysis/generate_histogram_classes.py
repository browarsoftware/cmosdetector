import cv2
def generate_plot(my_file, my_path):
    with open(my_file) as f:
        lines = f.read().splitlines()

    files = []
    classes = []
    mmax = []
    for ll in lines:
        files.append(ll.split("\t")[0])
        classes.append((ll.split("\t")[1]))
    print(files)
    path1 = my_path
    for ff in files:
        img = cv2.imread(path1 + ff)
        print(ff)
        img2 = np.zeros((img.shape[0], img.shape[1]))
        img2 = img2 + img[:, :, 0]
        img2 = img2 + img[:, :, 1]
        img2 = img2 + img[:, :, 2]
        mm = np.max(img2)
        mmax.append(mm)
    D_id = []
    for a in range(len(classes)):
        if classes[a] == 'D':
            D_id.append(a)
    D_id = np.array(D_id).astype(int)
    mmax = np.array(mmax)
    mmaxD = mmax[np.array(D_id)]

    L_id = []
    for a in range(len(classes)):
        if classes[a] == 'L':
            L_id.append(a)
    L_id = np.array(L_id).astype(int)
    mmaxL = mmax[np.array(L_id)]

    W_id = []
    for a in range(len(classes)):
        if classes[a] == 'W':
            W_id.append(a)
    W_id = np.array(W_id).astype(int)
    mmaxW = mmax[np.array(W_id)]
    return (mmaxD, mmaxL, mmaxW)

import matplotlib.pyplot as plt
import numpy as np

(mmaxD1, mmaxL1, mmaxW1) = generate_plot("data\\cropped\\rp1.3classes.txt", "data\\cropped\\rp13\\")
(mmaxD2, mmaxL2, mmaxW2) = generate_plot("data\\cropped\\rp2.0classes.txt", "data\\cropped\\rp20\\")

mmaxD = np.append(mmaxD1, mmaxD2)
mmaxL = np.append(mmaxL1, mmaxL2)
mmaxW = np.append(mmaxW1, mmaxW2)

plt.figure(figsize=(8,6))
plt.xlim([255, 765])
plt.hist(mmaxD, bins=20, alpha=0.5, label="Spot")
plt.hist(mmaxL, bins=20, alpha=0.5, label="Track")
plt.hist(mmaxW, bins=20, alpha=0.5, label="Worm")
plt.xlabel("Highest pixel value", size=14)
plt.ylabel("Count", size=14)
plt.title("Histogram of highest pixel value (by classes)")
plt.legend(loc='upper right')
plt.show()

print(len(mmaxD))
print(len(mmaxL))
print(len(mmaxW))

(mmaxD, mmaxL, mmaxW) = generate_plot("d:\\dane\\lapacz czastek\\cropped\\3ok.txt", "d:\\dane\\lapacz czastek\\cropped\\lapacz3\\")

plt.figure(figsize=(8,6))
plt.xlim([255, 765])
plt.hist(mmaxD, bins=20, alpha=0.5, label="Spot")
plt.hist(mmaxL, bins=20, alpha=0.5, label="Track")
plt.hist(mmaxW, bins=20, alpha=0.5, label="Worm")
plt.xlabel("Highest pixel value", size=14)
plt.ylabel("Count", size=14)
plt.title("Histogram of highest pixel value (by classes)")
plt.legend(loc='upper right')
plt.show()

print(len(mmaxD))
print(len(mmaxL))
print(len(mmaxW))
