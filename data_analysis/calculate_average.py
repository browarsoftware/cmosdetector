import glob
import cv2
import numpy as np

def generate_data(path):
    my_files = glob.glob(path)
    val = []
    #for my_file in my_files:
    for a in range(len(my_files)):
        my_file = my_files[a]
        img = cv2.imread(my_file)
        img2 = np.zeros((img.shape[0], img.shape[1]))

        img2 = img2 + img[:, :, 0]
        img2 = img2 + img[:, :, 1]
        img2 = img2 + img[:, :, 2]

        val.append(np.mean(img2))
    return val

val1 = generate_data(path = "d:\\path_to_raw_data\\*.png")

print(np.mean(np.array(val1)))
print(np.std(np.array(val1)))



