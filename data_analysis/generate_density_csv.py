import glob
import cv2
import numpy as np
import os

path = "d:\\path_to_raw_data\\*.png"
my_files = glob.glob(path)

values = np.zeros(255*3, dtype=int)

for my_file in my_files:
    try:
        img = cv2.imread(my_file)
        img_copy = np.copy(img)
        img2 = np.zeros((img.shape[0], img.shape[1]))
        print(my_file)
        img2 = img2 + img[:, :, 0]
        img2 = img2 + img[:, :, 1]
        img2 = img2 + img[:, :, 2]

        max_val = int(np.max(img2))
        values[max_val] = values[max_val] + 1
    #damaged feames
    except:
        print("##REMOVE## " + my_file)
        os.remove(my_file)
np.savetxt('rpXX.csv', values, delimiter=',')
