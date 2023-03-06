import glob
import cv2
import numpy as np
import os

path = "d:\\path_to_raw_data\\*.png"
path_to_save = "data\\cropped\\rpXX\\"

my_files = glob.glob(path)

for my_file in my_files:
    img = cv2.imread(my_file)
    img_copy = np.copy(img)
    id_X = 0
    id_Y = 0
    img2 = np.zeros((img.shape[0], img.shape[1]))

    img2 = img2 + img[:, :, 0]
    img2 = img2 + img[:, :, 1]
    img2 = img2 + img[:, :, 2]

    max_val = np.max(img2)
    avg_val = np.mean(img2)

    if max_val > 255:
        print(max_val)
        for a in range(img.shape[0]):
            for b in range(img.shape[1]):
                if img2[a, b] == max_val:
                    # img_copy[a,b,2] = 255
                    id_X = a
                    id_Y = b


        if id_X > 0 and id_Y > 0:
            img_copy = img[(id_X - 30): (id_X + 30), (id_Y - 30): (id_Y + 30), :]
        img_copy = cv2.resize(img_copy, [256, 256], interpolation=cv2.INTER_NEAREST).astype(np.uint8)

        my_file_save = os.path.basename(my_file)
        cv2.imwrite(path_to_save + my_file_save,  img_copy)

